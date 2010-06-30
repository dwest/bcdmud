import socket
import threading
from threading import Thread, Semaphore
import SocketServer
from multiprocessing import Pipe, Manager, Queue
from select import select

class ThreadedTCPRequestHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        p = self.server.chatserver.getPipe()
        self.data = ""
        while self.data != "bye":
            if p.poll():
                self.wfile.write(p.recv())

            readable, writable, error = select([self.request], [], [], 0)
            if self.request in readable:
                self.data = self.rfile.readline().strip()
                p.send("%s wrote: %s" % (self.client_address[0], self.data))

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    def setChatServer(self, chatserver):
        self.chatserver = chatserver

class ChatServer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.clients = list()
        self.lock = Semaphore()
        # Set this to false when you want to stop chat server
        self.RUNNING = True

    def run(self):
        while self.RUNNING:
            self.lock.acquire()
            for c in self.clients:
                try:
                    if c.poll():
                        self.relayMessage(c, c.recv())
                except EOFError:
                    # Poll apparently thinks it's cute to say that there is data on the pipe when it is closed
                    self.clients.remove(c)
            
            self.lock.release()

    def getPipe(self):
        server_side, client_side = Pipe()
        self.addPipe(server_side) # Blocks for an indeterminate amount of time
        return client_side

    def addPipe(self, connection):
        self.lock.acquire()
        self.clients.append(connection)
        self.lock.release()

    def relayMessage(self, client, message):
        # assuming that this will only be called by the chatserver's run method
        # also assuming that the client list is locked from modification
        for c in self.clients:
            if c is client:
                continue
            c.send(message)
    
if __name__ == "__main__":
    # Create the chat server to pass messages between clients
    chatserver = ChatServer()
    
    # Start the chat server
    chatserver.start()

    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Tell the socket server to use this chat server
    server.setChatServer(chatserver)

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.setDaemon(True)
    server_thread.start()
    print "Server Address:", ip, " ", port

    message = ""
    while message != "bye":
        message = raw_input("Type bye to exit: ")
        
    chatserver.RUNNING = False
    server.shutdown()
