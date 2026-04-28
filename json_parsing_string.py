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

names = []
scores = []


def skip_spaces(i):
    while i < len(data_string) and data_string[i].isspace():
        i += 1
    return i


def parse_string(i):
    i += 1
    res = []
    while i < len(data_string):
        if data_string[i] == '\\':
            i += 1
            if i < len(data_string):
                res.append(data_string[i])
        elif data_string[i] == '"':
            return ''.join(res), i + 1
        else:
            res.append(data_string[i])
        i += 1
    raise ValueError


def parse_number(i):
    start = i
    if data_string[i] == '-':
        i += 1
    while i < len(data_string) and data_string[i].isdigit():
        i += 1
    return int(data_string[start:i]), i


def parse(i=0):
    while i < len(data_string):
        i = skip_spaces(i)
        if i >= len(data_string):
            break
        c = data_string[i]
        if c in '[{':
            i = parse(i + 1)
        elif c in ']}':
            return i + 1
        elif c == '"':
            key, i = parse_string(i)
            i = skip_spaces(i)
            i += 1
            i = skip_spaces(i)
            if key == "fullName":
                val, i = parse_string(i)
                names.append(val)
            elif key == "points":
                val, i = parse_number(i)
                scores.append(val)
            elif key == "child":
                i = parse(i)
            else:
                if data_string[i] == '"':
                    _, i = parse_string(i)
                elif data_string[i] in '{[':
                    i = parse(i + 1)
                else:
                    while i < len(data_string) and data_string[i] not in ',}]':
                        i += 1
        else:
            i += 1
    return i


parse()

average = sum(scores) / len(scores)

print("Names:")
for n in names:
    print(n)

print(f"\nHere is the scores of provided people: {scores}")
print(f"Here is the average score of provided people: {average}")
