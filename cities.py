import csv
def compare(a, op, b):
    if op == "<":
        return a < b
    if op == ">":
        return a > b
    if op == "<=":
        return a <= b
    if op == ">=":
        return a >= b
    if op == "==":
        return a == b


with open('worldcities.csv', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))

query = input().lower()

if ">=" in query:
    op = ">="
elif "<=" in query:
    op = "<="
elif "==" in query:
    op = "=="
elif ">" in query:
    op = ">"
elif "<" in query:
    op = "<"
else:
    print("Invalid operator")
    exit()

parts = query.split(op)
field = parts[0].strip()
value = parts[1].strip()

if field not in reader[0].keys() and field != "city":
    print("Invalid field")
    exit()
if field in ["population", "lat", "lng"]:
    try:
        float(value)
    except ValueError:
        print("Invalid operator")
        exit()
if field == "city" and op != "==":
    target = None
    for row in reader:
        if row["city"].lower() == value:
            try:
                target = int(float(row["population"]))
                break
            except:
                continue

    if target is None:
        print("City not found")
        exit()

    for row in reader:
        try:
            pop = int(float(row["population"]))
            if compare(pop, op, target):
                print(row)
        except:
            continue
else:
    for row in reader:
        try:
            if field == "population":
                a = int(float(row[field]))
                b = int(float(value))
            elif field == "lat" or field == "lng":
                a = float(row[field])
                b = float(value)
            else:
                a = row[field].lower()
                b = value

            if compare(a, op, b):
                print(row)
        except:
            continue