import collections
from collections import defaultdict
from read_data import flatten

import json

#f = open('./apt_show_data.txt','r')
f = open('./final.json','r')
data = f.read()
data = json.loads(data)
f.close()

feature_set = set()

for key, value in data.items():
    for k in value.keys():
        feature_set.add(k)


final_features = list(feature_set)
print(final_features)
print(len(final_features))

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

f = open('final_data_apt.json', 'w')
f.write(json.dumps(dct, indent=4))
f.close()


## Making TSV

f = open('final_data_apt.tsv', 'w')
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
