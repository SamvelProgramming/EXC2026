count = 0
lst = []
for i in range(1234, 6789):
    d = i
    while d != 0:
        digit = d % 10
        d //= 10
        lst.append(digit)
    print(lst)
    copy = lst.copy()
    sort = sorted(copy)
    if copy[::-1] == sort:
        count += 1
        copy.clear()
        lst.clear()
        sort.clear()
print(count)
