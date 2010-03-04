import json

#message type
ACTION, MESSAGE, ADMIN = range(3)

#valid actions
actions = ['move', 'cast', 'use', 'do']
messageTypes = ['say', 'yell', 'party']
adminOps = ['connect', 'gamelist', 'update', 'start']

class ClientMessage:
    """Takes a JSON encoded string and attempt to turn it 
    into a valid message, throws exception if it can't."""
    mtype = None
    mpayload = dict()
    valid = False

    def __init__(self, message):
        try:
            data = json.loads(message)
        except ValueError:
            self.valid = False
            raise InvalidMessageError

        if 'action' in data:
            self.mtype = ACTION
            self.validate(actions, data['action'])
        elif 'message' in data:
            self.mtype = MESSAGE
            self.validate(messageTypes, data['message'])
        elif 'admin' in data:
            self.mtype = ADMIN
            self.validate(adminOps, data['admin'])
        else:
            self.valid = False
            raise InvalidMessageError

    def validate(self, validItems, payload):
        for item in validItems:
            if item in payload:
                self.mpayload = {item: payload[item]}
                return
        
        self.valid = False
        raise InvalidMessageError

class InvalidMessageError(Exception):

    def __init__(self, value="Invalid Message"):
        self.value = value

    def __str__(self):
        return repr(self.value)
