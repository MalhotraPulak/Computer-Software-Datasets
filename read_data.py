import collections
from collections import defaultdict

import json


def flatten(d, parent_key='', sep='|'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

f = open('data.json',)
data = json.load(f)

count_of_keys = defaultdict(int)

for k,v in data.items():
    new_item = flatten(v)
    for new_keys in new_item.keys():
        if new_item[new_keys] is not None:
            count_of_keys[new_keys]+=1


for k,v in sorted(count_of_keys.items(), key=lambda item: item[1],reverse=True):
    if v > 10:
        print(k + " " + str(v))
