import json
data = json.load(open("data.json"))


def return_definition(input):
  response = input
  return f"You typed in {response}"

print(return_definition("hey"))