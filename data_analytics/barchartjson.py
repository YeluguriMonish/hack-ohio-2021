import json

def create_bargraph_json(file, saveFile):
    with open(file) as f:
        data = json.load(f)
    barGraphData = []
    for item in data[0:5]:
        dict = {}
        dict["name"] = item["first_name"]+" "+item["last_name"]
        dict["TRx"] = item["TRx_sum"]
        barGraphData.append(dict)
    with open(saveFile, 'w') as outFile:
        json.dump(barGraphData, outFile)

create_bargraph_json('data/topSellersCholecap.json', 'data/bargraphCholecap.json')
create_bargraph_json('data/topSellersNasalclear.json', 'data/bargraphNasalclear.json')
create_bargraph_json('data/topSellersNova_itch.json', 'data/bargraphNova_itch.json')
create_bargraph_json('data/topSellersZap_a_Pain.json', 'data/bargraphZap_a_Pain.json')
