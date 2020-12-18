import json
data = json.load(open("data.json"))


def return_definition(word):
  return data[word]

word = input("Enter word: ")

print(return_definition(word))