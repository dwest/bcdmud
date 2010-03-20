from multiprocessing import Process
from ClientMessage import *
import socket
import sys

MAXMSGLEN = 1048576
DELIMITER = "\n"

class GameConnection(Process):
    clientSocket = None
    gameServer = None
    clientAddress = None
    proxy = None

    def __init__(self, server, socket, instance):
        Process.__init__(self)
        self.clientSocket = socket
        self.gameServer = server
        self.proxy = ServerProxy(self, self.gameServer, instance)
        print "New connection:",self.clientSocket.getpeername()

    def run(self):
        if self.clientSocket is None or self.gameServer is None:
            return
        
        message = ""
        while len(message) < MAXMSGLEN:
            while 1:
                data = self.clientSocket.recv(1024)
                if not data: break #socket is now closed
                message += data
                m, p, r = message.partition(DELIMITER)
                if p != '':
                    try:
                        cMessage = ClientMessage(m)
                        self.proxy.handleMessage(cMessage)
                    except InvalidMessageError:
                        print "Invalid Message from client: "+repr(self.clientSocket.getpeername())
                    message = r
            return 

    def send(self, message):
        self.clientSocket.send(message)

    def close(self):
        self.clientSocket.shutdown(socket.SHUT_RDWR)
        self.clientSocket.close()

"""
        while len(message) < MAXMSGLEN:
            while 1:
                data = self.clientSocket.recv(1024)
                if not data: break #socket is now closed
                else:
                    try:
                        cMessage = ClientMessage(m)
                        print cMessage
                    except InvalidMessageError:
                        print "Invalid Message from client: "+repr(self.clientSocket.getpeername())
                        return
"""
