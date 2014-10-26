import json
from pprint import pprint
json_data=open('json_data.json')

data = json.load(json_data)
print(data["om_points"])
pprint(data)
json_data.close()
