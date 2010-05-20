import socket
import json

class Proxy:

    socket = None
    inputType = {'w': ("move", 0),
                 'a': ("move", 3),
                 's': ("move", 2),
                 'd': ("move", 1),
                 }

    def __init__(self, HOST, PORT):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((HOST,PORT))
        except socket.error, msg:
            print "Exception thrown trying to connect to remote address "
            print msg

    def handleInput(self, input):
        if input in self.inputType:
            msg = self.inputType[input]
            if msg[0] == "move":
                self.action(msg)

    def action(self, action):
        """
        Example: {"action": {"move": 0}}
          ^
          0
        <3 1>
          2
          v
        Encode move action and send to server
        Perhaps we should store all available actions 
        in DB, but IDK that would require query every startup
        """
        (type, dir) = action
        action = json.dumps({"action": {type: dir}})
        self.sendRequest("action", action)

    def message(self, vol, msg):
        """
        Example: {"message": {"yell": "Hello World"}}
        """
        say = json.dumps({"message": {vol: msg}})
        self.sendRequest("message", say)

    def sendRequest(self, type, req):
        """
        Append every message with \n for use with
        DELIMITER in GameConnection
        """
        try:
            self.socket.sendall(req+'\n')
        except socket.error, msg:
            print "Exception thrown on "+type+" ",msg

    def close(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
