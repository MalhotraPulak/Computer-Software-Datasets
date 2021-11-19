import collections
from collections import defaultdict

import json


def flatten(d, top_key, parent_key="", sep="|"):
    items = []
    for k, v in d.items():
        k = k.replace(top_key, "command")
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, top_key, new_key, sep=sep).items())
        elif isinstance(v, list):
            v = {str(k_temp): v_temp for k_temp, v_temp in enumerate(v)}
            items.extend(flatten(v, top_key, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


f = open("data-cask.json", "r")
data = json.load(f)
f.close()

count_of_keys = defaultdict(int)
list_of_all_packages = []
list_of_features = []
for k, v in data.items():
    new_item = flatten(v, k)
    for new_keys in new_item.keys():
        if new_item[new_keys] is not None and new_item[new_keys]:
            count_of_keys[new_keys] += 1
    list_of_all_packages.append(new_item)

for k, v in sorted(
    count_of_keys.items(), key=lambda item: item[1], reverse=True
):
    if v > 500:
        list_of_features.append(k)

print(len(list_of_all_packages))
print(len(list_of_features))


## Making TSV

f = open("brew_data-cask.tsv", "w")
heading = ""
for feature in list_of_features:
    heading += feature + "\t"

f.write(heading[:-1] + "\n")


for item in list_of_all_packages:
    entry = ""
    for feature in list_of_features:
        if item.get(feature):
            entry += str(item[feature]) + "\t"
        else:
            entry += "\t"

    f.write(entry[:-1] + "\n")

f.close()
