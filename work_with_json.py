# JSON -JavaScript Object Notation

import json
from random import randint
from datetime import datetime
str_json = '''
{
"response": {
        "count":5961878,
        "items": [{
            "first_name": "Norbert",
            "id": 620471795,
            "last_name": "Bober",
            "can_access_closed": true,
            "is_closed": false,
            "photo_50": "https://sun1-99.u...nC7eC9Cd4&ava=1"
        }, {
            "first_name": "Deget",
            "id": 614752515,
            "last_name": "Bober",
            "can_access_closed": true,
            "is_closed": false,
            "photo_50": "https://sun1-93.u...Ylb-6CPfo&ava=1"
}]
}  
}'''
print(type(str_json))

# function to deserialize a JSON string into Python object
data = json.loads(str_json)
print(type(data))
print(type(data['response']['items']))

for item in data['response']['items']:
    print(type(item))
    print(item['first_name'],item['last_name'])
    del item ['id'] # delete key
    item['likes'] = randint(100, 200) # add new key
    item['a'] = None
    # make a special format for datetime
    item['now'] = datetime.now().strftime('%d.%m.%y')
print(data['response']['items'])


# function to serialize a Python object to JSON string
new_json = json.dumps(data, indent=2)
print(new_json)
