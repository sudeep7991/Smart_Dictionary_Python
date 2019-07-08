
import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        check = input("Did you mean '%s' instead? Enter Yes or No : " %get_close_matches(w,data.keys())[0])
        if check in ["Y","y","yes"]:
            return data[get_close_matches(w,data.keys())[0]]
        elif check in ["N","n","no"]:
            return "Word not found! Please double check."
        else:
            return "Please enter the correct input"
    else:
        return "Word not found! Please double check."


word = input("Enter a word: ")

out = meaning(word)

if type(out) == list :
    for i in out:
        print("-> "+i)
else:
    print(out)
