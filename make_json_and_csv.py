import collections
from collections import defaultdict
from read_data import flatten

import json

f = open('data.json','r')
data = json.load(f)
f.close()

f = open('list_of_keys','r')
features = f.read()
f.close()

features_lst = [feature for feature in features.split("\n")]

final_features = []

for feature in features_lst:
    feature = feature.split(" ")[0]
    final_features.append(feature)

## Making JSON

dct = {}

for k,v in data.items():
    new_item = flatten(v,k)

    inner_dct = {}
    for feature in final_features:
        if new_item.get(feature):
            inner_dct.update({feature: new_item[feature]})
        else:
            inner_dct.update({feature: " "})
    
    dct.update({k: inner_dct})

f = open('final_data.json', 'w')
f.write(json.dumps(dct, indent=4))
f.close()


## Making CSV

f = open('final_data.csv', 'w')
heading = ""
for feature in final_features:
    heading += feature + "\t"

f.write(heading[:-1]+"\n")

for k,v in data.items():
    new_item = flatten(v,k)
    entry = ""
    for feature in final_features:
        if new_item.get(feature):
            entry += str(new_item[feature]) + "\t"
        else:
            entry += "\t"
    
    f.write(entry[:-1]+"\n")

f.close()
