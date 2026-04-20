n = int(input("Enter arrester's number: "))
s = int(input("Enter sit i should start: "))
m = int(input("Enter how many chocolates do i got: "))
s = 2
arr = []
i = 0
while m > 0:
    if i < n:
        arr.append((s + i - 1) % n + 1)
        i += 1
        m -= 1
    else:
        arr.append((s - 1) % n + 1)
        s += 1
        m -= 1
print(f"Bad luck: {arr[-1]}")