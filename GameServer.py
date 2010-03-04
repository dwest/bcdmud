from multiprocessing import Process, Queue
from GameConnection import *
from ClientMessage import *
import socket
import sys

class GameServer:
    activeConnections = set()
    activeGames = dict()
    listeningSocket = None
    
    def __init__(self, HOST, PORT):
        try:
            self.listeningSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listeningSocket.bind((HOST, PORT))
        except socket.error, msg:
            print "Exception thrown trying to bind port: "
            print msg

    def host(self):
        if self.listeningSocket is None:
            print "Unable to host on empty socket!"
            return

        self.listeningSocket.listen(5)

        try:
            while 1:
                (clientsocket, address) = self.listeningSocket.accept()
                connection = GameConnection(self, clientsocket)
                self.activeConnections.add(connection)
                connection.start()
        except KeyboardInterrupt:
            for s in self.activeConnections:
                s.close()
            self.listeningSocket.close()

    def handleMessage(self, connection, message):
        if connection not in activeConnections:
            connection.close()

        if connection.gameInstance is not None:
            connection.gameInstance.handleMessage(connection, message)

        if message.mtype == ClientMessage.ADMIN:
            if 'connect' in message:
                self.connect(connection, message['connect'])
            elif 'gamelist' in message:
                self.listGames(connection)
