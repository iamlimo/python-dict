import json
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return   return data[word][0]
    else:
        return "The word doesn't exist"

print(translate("love"))