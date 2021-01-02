import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def return_definition(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif len(get_close_matches(w, data.keys())) > 0:
    return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
  else:
    return "Word does not exist. Please check again."

word = input("Enter word: ")

print(return_definition(word))