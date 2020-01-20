import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate():
    word = input("Enter a world: ")
    if word in data:
       return data[word][0]
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestWord = input("Do you mean? %s : " % get_close_matches(word, data.keys())[0])
        if (suggestWord == "Yes"):
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Word doesnt exist"
    else:
        return "The word doesn't exist"
options = translate()

if type(options) == list:
    for item in options:
        print(item)
else:
    print(options)

