from ClientMessage import *
from GameServer import *
from Game import *

class ServerProxy:
    """Takes a client message and calls the appropriate functions on the
    provided server, and game instance."""
    client = None
    server = None
    instance = None

    def __init__(self, client, server, instance=None):
        self.client = client
        self.server = server
        self.instance = instance

    def handleMessage(self, message):
        #must be an instance of ClientMessage for any of these calls to work...
        if not type(message) is ClientMessage or not type(message.payload) is dict:
            raise InvalidMessageError

        if message.mtype == None:
            return False

        if message.mtype == ClientMessage.ACTION:
            self.doAction(message.mpayload)
        elif message.mtype == ClientMessage.MESSAGE:
            self.doMessage(message.mpayload)
        elif message.mtype == ClientMessage.ADMIN:
            self.doAdmin(message.mpayload)
        else:
            raise InvalidMessageError

    def doAction(self, action):
        if 'move' in action:
            self.instance.playerMove(client, action['move'])
        elif 'cast' in action:
            self.instance.playerCast(client, action['cast'])
        elif 'use' in action:
            self.instance.playerUse(client, action['use'])
        elif 'do' in action:
            self.instance.playerDo(client, action['do'])
        else:
            raise InvalidMessageError

    def doMessage(self, message):
        for t in ClientMessage.messageTypes:
            if t in message:
                self.instance.playerMessage(t, message[t])
                break
        raise InvalidMessageError

    def doAdmin(self, operation):
        if client is None and not 'register' in operation and not 'auth' in operation:
            raise InvalidMessageError

        if not client is None and 'auth' in operation:
            raise InvalidMessageError

        if 'username' in operation and 'password' in operation:
            if 'auth' in operation:
                self.client = self.server.auth(operation['username'], operation['password'])
                if self.client is None: return False
            elif 'register' in operation:
                self.client = self.server.register(operation['username'], operation['password'])
                if self.client is None: return False
            raise InvalidMessageError

        if 'gamelist' in operation:
            return self.server.gamelist()

        if 'connect' in operation:
            if 'game_id' in operation:
                self.server.connect(self.client, operation['game_id'])
            raise InvalidMessageError

        if 'start' in operation:
            gameData = operation['start']
            if not type(gameData) is dict:
                raise InvalidMessageError
            if 'name' in gameData:
                if 'private' in gameData:
                    self.server.start(self.client, gameData['name'], gameData['private'])
                else:
                    self.server.start(self.client, gameData['name'])
            else:
                raise InvalidMessageError
        
        if 'connect' in operation:
            gameData = operation['start']
            if not type(gameData) is dict:
                raise InvalidMessageError
            if 'id' in gameData:
                if 'private' in gameData:
                    self.server.connect(self.client, gameData['id'], gameData['private'])
                else:
                    self.server.connect(self.client, gameData['id'])
            else:
                raise InvalidMessageError

