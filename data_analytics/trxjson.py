import json

TRx_columns = ['TRx_Month_1','TRx_Month_2','TRx_Month_3','TRx_Month_4','TRx_Month_5','TRx_Month_6']

with open('src/data/sums.json') as f:
    data = json.load(f)
for item in data:
    trxData = []
    index = 1
    name = item["Product"]
    name = name.replace('-', '_')
    for column in TRx_columns:
        dict = {}
        dict["name"] = str(index)
        dict["prescriptions"] = item[column]
        index = index+1
        trxData.append(dict)
    with open('src/data/TRx' + name + '.json', 'w') as outFile:
        json.dump(trxData, outFile)
