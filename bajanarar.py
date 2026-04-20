a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)