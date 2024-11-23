import json

class JsonError:
    code = 0
    message = ""    

    def __init__(self, cod, mes):
        self.code = cod
        self.message = mes

    def getJson(self):
        return self.__dict__

