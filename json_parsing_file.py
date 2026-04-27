import json

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except:
    print("Error: data.json not found.")

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
