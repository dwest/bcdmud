import socket
import threading
from threading import Thread, Semaphore
import SocketServer
from multiprocessing import Pipe, Manager, Queue
from select import select
from copy import deepcopy
import json

from tmp_mapgen import *

class ThreadedTCPRequestHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        p = self.server.chatserver.getPipe()
        q = self.server.gameserver.getPipe()

        self.data = ""
        while self.data != "bye":
            if p.poll():
                self.wfile.write(p.recv())

            if q.poll():
                self.wfile.write(q.recv())

            readable, writable, error = select([self.request], [], [], 0)
            if self.request in readable:
                self.data = self.rfile.readline().strip()
                p.send(self.data)
                q.send(self.data)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    def setChatServer(self, chatserver):
        self.chatserver = chatserver

    def setGameServer(self, gameserver):
        self.gameserver = gameserver

class ChatServer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.clients = list()
        self.lock = Semaphore()
        # Set this to false when you want to stop the chat server
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
        print "----"
        print message
        print "----"

        message = json.dumps(message)
        if 'say' not in message:
            return 

        # assuming that this will only be called by the chatserver's run method
        # also assuming that the client list is locked from modification
        for c in self.clients:
            if c is client:
                continue
            c.send(message['say'])

class GameServer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.clients = list()
        self.map = make_level()
        self.locations = {}
        self.lock = Semaphore()
        # Set this to false when you want to stop the game server
        self.RUNNING = True

    def run(self):
        while self.RUNNING:
            self.lock.acquire()
            for c in self.clients:
                try:
                    if c.poll():
                        self.handleMessage(c, c.recv())
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

    def movePlayer(self, client, direction):
        if self.clients.index(client) in self.locations:
            curr_location = self.locations[self.clients.index(client)]
        else:
            for i in range(0, len(self.map)):
                for j in range(0, len(self.map[i])):
                    if self.map[i][j] == 1:
                        curr_location = (i, j)
        
        if direction == "LEFT":
            for others in self.locations:
                if self.locations[others][1] == curr_location[1]-1 and self.locations[others][0] == curr_location[0]:
                    return
            if self.map[curr_location[0]][curr_location[1]-1] == 1:
                curr_location = (curr_location[0], curr_location[1]-1)
        elif direction == "RIGHT":
            for others in self.locations:
                if self.locations[others][1] == curr_location[1]+1 and self.locations[others][0] == curr_location[0]:
                    return
            if self.map[curr_location[0]][curr_location[1]+1] == 1:
                curr_location = (curr_location[0], curr_location[1]+1)
        elif direction == "UP":
            for others in self.locations:
                if self.locations[others][0] == curr_location[0]-1 and self.locations[others][1] == curr_location[1]:
                    return
            if self.map[curr_location[0]-1][curr_location[1]] == 1:
                curr_location = (curr_location[0]-1, curr_location[1])
        elif direction == "DOWN":
            for others in self.locations:
                if self.locations[others][0] == curr_location[0]+1 and self.locations[others][1] == curr_location[1]:
                    return
            if self.map[curr_location[0]+1][curr_location[1]] == 1:
                curr_location = (curr_location[0]+1, curr_location[1])

        self.locations[self.clients.index(client)] = curr_location
        return

    def getGameState(self):
        output = deepcopy(self.map)

        for i in range(0, len(output)):
            for j in range(0, len(output[i])):
                if output[i][j] == 0:
                    output[i][j] = '#'
                else:
                    output[i][j] = '.'

        for location in self.locations:
            location = self.locations[location]
            output[location[0]][location[1]] = '@'

        s = ""
        for row in output:
            s += ''.join(row)
            s += '\n'
        
        return s

    def handleMessage(self, client, message):
        # message should be a json encoded object
        try:
            message = json.loads(message)
            if "move" in message:
                self.movePlayer(client, message['move'])
                print self.getGameState()
                client.send(self.getGameState())
        except ValueError:
            pass

if __name__ == "__main__":
    # Create the chat server to pass messages between clients
    chatserver = ChatServer()
    chatserver.start()

    # Create the game server to store game state
    gameserver = GameServer()
    gameserver.start()

    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Tell the socket server to use this chat server
    server.setChatServer(chatserver)
    server.setGameServer(gameserver)

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
    gameserver.RUNNING = False
    server.shutdown()
