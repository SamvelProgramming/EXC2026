n = int(input("Enter a number: "))
i = 1
number = 1
arr = [1]
while i != n:
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        arr.append(number)
        i += 1
    number += 1
print(arr[n - 1])