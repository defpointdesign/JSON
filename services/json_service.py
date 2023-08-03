import json

class JsonService:
    ''' Function for working with JSON files'''
    def readFile(name):
        with open(name, 'r') as file:
            return json.load(file)
    def writeFile(name, data):
        with open(name, 'w') as file:
            return json.dump(data, file )


