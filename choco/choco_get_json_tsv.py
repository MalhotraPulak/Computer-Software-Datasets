import collections
from collections import defaultdict

import json

def flatten(d,top_key,parent_key='', sep='|'):
    items = []
    for k, v in d.items():
        k = k.replace(top_key,'command')
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v,top_key ,new_key, sep=sep).items())
        elif isinstance(v, list):
            v = {str(k_temp): v_temp for k_temp, v_temp in enumerate(v)}
            items.extend(flatten(v,top_key ,new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

f = open('./choco_data.json','r')
#f = open('./final.json','r')
data = f.read()
data = json.loads(data)
f.close()

feature_set = set()

for dct in data:
    for key in dct.keys():
        feature_set.add(key)

final_features = list(feature_set)
print(final_features)
print(len(final_features))

## Making TSV

f = open('choco_data.tsv', 'w')
heading = ""
for feature in final_features:
    heading += feature + "\t"

f.write(heading[:-1]+"\n")

for new_item in data:
#    new_item = flatten(v,k)
    entry = ""
    for feature in final_features:
        if new_item.get(feature):
            entry += str(new_item[feature]) + "\t"
        else:
            entry += "\t"
    
    f.write(entry[:-1]+"\n")

f.close()
