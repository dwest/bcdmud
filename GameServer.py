import SocketServer
import Queue
import multiprocessing
from multiprocessing import Queue, Process

from ClientMessage import *
from ServerProxy import *

class TCPHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        # Toss request on queue
        gameQueue.put(self.request.recv(4096))

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    def setQueueProcess(self, queue):
        self.queueProcess = queue

class QueueProcess(Process):

    def __init__(self, queue, proxy):
        Process.__init__(self)
        self.queue = queue

    # Get next item from queue
    # Create ClientMessage obj
    def run(self):
        while True:
            item = self.queue.get()
            try:
                message = ClientMessage(item)
            except InvalidMessageError, err_msg:
                print ""
                print err_msg, item


# Create and start the class that will process 
# items on the queue
gameQueue = Queue()
p = QueueProcess(gameQueue)
p.start()

# Create server proxy


# Create the server 
HOST, PORT = "localhost", 0
server = ThreadedTCPServer((HOST, PORT), TCPHandler)
server.setQueueProcess(p)
server_process = Process(target=server.serve_forever)
server_process.daemon = True
server_process.start()

ip, add = server.server_address
print ip," ",add


# Show the server CLI
# TODO: Make ServerCLI class!
message = ""
while message != 'bye':
    try:
        message = raw_input(">> ")
    except EOFError:
        break

print "\n"
p.terminate()
server_process.terminate()
