from os import listdir
import json
import collections

def flatten(d,parent_key='', sep='|'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v,new_key, sep=sep).items())
        elif isinstance(v, list):
            v = {str(k_temp): v_temp for k_temp, v_temp in enumerate(v)}
            items.extend(flatten(v,new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


list_of_all_packages = []

list_of_files = listdir('./data-api')
for file_name in list_of_files:
    f = open("./data-api/"+file_name,)
    data = json.load(f)
    for item in data['results']:
        list_of_all_packages.append(flatten(item))

total_packages  = len(list_of_all_packages)

feature_set = collections.defaultdict(int)

for value in list_of_all_packages:
    for k in value.keys():
        if value[k]:
            feature_set[k]+=1

temp = dict(sorted(feature_set.items(), key=lambda item: item[1],reverse=True))
list_of_features = []
i=0
for item in temp:
    list_of_features.append(item)
    i+=1
    if i>=30:
        break
print(list_of_features)


## Making TSV

f = open('macports_data.tsv', 'w')
heading = ""
for feature in list_of_features:
    heading += feature + "\t"

f.write(heading[:-1]+"\n")


for item in list_of_all_packages:
    entry=""
    for feature in list_of_features:
        if item.get(feature):
            entry += str(item[feature]) + "\t"
        else:
            entry += "\t"
    
    f.write(entry[:-1]+"\n")

f.close()
