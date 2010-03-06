import socket
import json

class Proxy:

    socket = None

    def __init__(self, HOST, PORT):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((HOST,PORT))
        except socket.error, msg:
            print "Exception thrown trying to connect to remote address "
            print msg

    def action(self, type, dir):
        """
        Example: {"action": {"move": 0}}

        Encode move action and send to server
        Perhaps we should store all available actions 
        in DB, but IDK that would require query every startup
        """
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
