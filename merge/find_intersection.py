import json

intersection_dct = {}

def make_dct(content):
    for k in content:
        if intersection_dct.get(k):
            val = intersection_dct[k]
            intersection_dct[k] = val+1
        else:
            intersection_dct[k] = 1

#f = open('data.json', 'r')
#content = f.read()
#content = json.loads(content)
#keys = content.keys()
#make_dct(keys)
#f.close()


f = open('apt_show_data.txt', 'r')
content = f.read()

keys = []
for line in content.split("\n"):
    if line!="":
        my_line = json.loads(line)
        pkg_name = my_line['Package']
        keys.append(pkg_name)
    
make_dct(keys)
f.close()


f = open('macports/ports_list.txt', 'r')
content = f.read()

keys = []
for line in content.split("\n"):
    words = line.split(" ")
    pkg_name = words[0]
    keys.append(pkg_name)

make_dct(keys)
f.close()

#print(intersection_dct)
cnt=0
for k,v in intersection_dct.items():
    if v>1:
        cnt+=1

print(cnt)
print(len(intersection_dct))
