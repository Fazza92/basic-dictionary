import json
data = json.load(open("data.json"))


def return_definition(word):
  word = word.lower()
  if word in data:
    return data[word]
  else:
    return "Word does not exist. Please check again."

word = input("Enter word: ")

print(return_definition(word))