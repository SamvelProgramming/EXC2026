import json

data_string = """[
  {
    "fullName": "John Smith",
    "points": 20,
    "child": {
      "fullName": "Michael Brown",
      "points": 25,
      "child": {
        "fullName": "David Wilson",
        "points": 14
      }
    }
  },
  {
    "fullName": "Emma Johnson",
    "points": 30
  },
  {
    "fullName": "Olivia Davis",
    "points": 22,
    "child": {
      "fullName": "James Miller",
      "points": 18
    }
  }
]"""

data = json.loads(data_string)

names = []
scores = []

def flatten(person):
    names.append(person["fullName"])
    scores.append(person["points"])

    if "child" in person and person["child"] != None:
        flatten(person["child"])

for j in data:
    flatten(j)

length = len(scores)
total = 0

for i in scores:
    total += i
    
average = total / length

print(f"Here is the names of provided people: {names}")
print(f"Here is the scores of provided people: {scores}")
print(f"Here is the average score of provided people: {average}")