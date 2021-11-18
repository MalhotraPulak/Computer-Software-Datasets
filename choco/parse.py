import pprint

with open("./stat_good.txt", "r", errors="ignore") as f:
    data = f.readlines()
data = [x.strip() for x in data]
package_lines = []
term = "Title:"
idx = 1
while idx != -1:
    start = idx - 1
    end = len(data)
    nidx = -1
    for j in range(idx + 1, len(data), 1):
        if term in data[j]:
            nidx = j
            end = j - 2
            break
    package_lines.append(data[start : end + 1])
    idx = nidx


def process_until(line, js):
    token = line.split(":")[0]
    js[token] = line.split(":", maxsplit=1)[1].strip()


processed_data = []
for lines in package_lines:
    fields = lines[0].split(" ")
    js = {}
    js["package_name"] = fields[0].strip()
    js["version"] = fields[1].strip()

    # Title and published
    fields = lines[1].split("|")
    js["title"] = fields[0].split(":")[1].strip()
    if len(fields) > 1 and ":" in fields[1]:
        js["published"] = fields[1].split(":")[1].strip()
    else:
        js["published"] = "NA"

    # approved by
    js["approved_by"] = "NA"
    js["approved_on"] = "NA"
    for l in lines:
        if "approved by" in l:
            rhs = l.split("approved by")[1].strip()
            by = rhs.split("on")[0]
            on = rhs.split("on")[1]
            js["approved_by"] = by.strip()
            js["approved_on"] = on.strip()
            break

    # testing status
    for l in lines:
        if "testing status" in l:
            process_until(l, js)
            break

    # Number of Downloads
    word = "Number of Downloads"
    for l in lines:
        if word in l:
            rhs = l.split(word + ": ")[1]
            cnt = rhs.split(" ")[0]
            js[word] = int(cnt)

    # Number of Downloads
    word = "Downloads for this version"
    for l in lines:
        if word in l:
            rhs = l.split(word + ": ")[1]
            cnt = rhs.split(" ")[0]
            js[word] = int(cnt)

    # Tags
    for l in lines:
        if "Tags:" in l:
            rhs = l.split(":")[1]
            tags = rhs.split(" ")
            if tags[0] == "":
                tags = tags[1:]
            js["tags"] = tags

    # extras
    extras = [
        "Software Site:",
        "Software License:",
        "Software Source:",
        "Documentation:",
        "Mailing List:",
        "Issues:",
        "Summary:",
        "Chocolatey Package Source:",
        "Package Checksum:",
        "Release Notes:",
    ]
    for l in lines:
        for w in extras:
            if w in l:
                process_until(l, js)

    # Description
    js["description"] = ""
    started = False
    for l in lines:
        if started:
            if "Release Notes:" in l:
                break
            js["description"] += f" {l.strip()}"
            continue

        if "Description:" in l:
            started = True
            rhs = l.split("Description: ")[1]
            js["description"] += rhs.strip()

    processed_data.append(js)

import json

with open("choco_data.json", "w") as f:
    json.dump(processed_data, f, indent=2)
# pprint.pprint(processed_data[:50])
# pprint.pprint(processed_data[1500:1700])
# print(processed_data[-50:])
