# elements = int(input("Enter elements number: "))
# cities = [int(input(f"Enter element {i}: ")) for i in range(elements)]
cities = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1]
k = int(input("Enter a radius for : "))
n = len(cities)
count = 0
i = 0
k = 3
while i < n:
    j = min(i + k - 1, n - 1)
    pos = -1
    while j >= i - k + 1 and j >= 0:
        if cities[j] == 1:
            pos = j
            break
        j -= 1
    if pos != -1:
        count += 1
        i = pos + k
    else:
        count = -1
        break
print(f"We need at least {count}")