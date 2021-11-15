import subprocess
import json

with open("temp.txt", "r") as f:
    data = f.readlines()


def toJson(details):
    details = details.split("\n")
    dic = {}
    prev = ""
    for line in details:
        if ":" in line:
            field = line.split(":")[0]
            desc = line.split(":")[1]
            dic[field] = desc[1:]
            prev = field
        else:
            dic[prev] += f" {line}"
    return dic


for i, x in enumerate(data):
    if i % 3 == 2:
        package = x.split("/")[0]
        print(f"{i//3 + 1} {package}")
        bashCommand = f"apt show {package}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        details = output.decode("utf-8")
        details = toJson(details)
        s = json.dumps(details)
        with open("final.txt", "a") as f:
            f.write(s + "\n")
