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

data = json.loads(str_json)

for item in data['response']['items']:
    del item ['id'] # delete key
    item['likes'] = randint(100, 200) # add new key
    item['a'] = None
    item['now'] = datetime.now().strftime('%d.%m.%y')

# create file
with open('my.json','w') as file:
    # function to serialize a Python object and write it to a JSON file.
    json.dump(data, file, indent=3)