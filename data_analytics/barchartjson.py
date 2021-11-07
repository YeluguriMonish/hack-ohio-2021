import json

def create_bargraph_json(file):
    with open(file) as f:
        string = json.dump(f)
        data = json.loads(string)
    print(data)

create_bargraph_json('data/topSellersCholecap.json')