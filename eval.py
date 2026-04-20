a = input("Enter a expression: ")
action = list(a)
numbers = list(a)
print(action)
print(numbers)
for char in action:
    if char.isdigit():
        action.remove(char)
for char in numbers:
    if not char.isdigit():
        numbers.remove(char)
print(action)
print(numbers)
total = int(numbers[0])
for i in range(1, len(numbers)):
    if action[i - 1] == "+":
        total += int(numbers[i])
    elif action[i - 1] == "-":
        total -= int(numbers[i])
    elif action[i - 1] is None:
        print(action[i - 1])
        action.remove(action[i - 1])
    else:
        print("Error")
        break
print(total)
