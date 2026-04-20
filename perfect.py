n = int(input("Enter n number: "))
count = 0
number = 1
while count < n:
    arr = []
    for i in range(1, number):
        if number % i == 0:
            arr.append(i)
    if sum(arr) == number:
        count += 1
    number += 1
print(number - 1)