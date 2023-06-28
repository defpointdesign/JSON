import json

with open('my.json', 'r') as file:
    data = json.load(file)
print(type(data))
print(data)