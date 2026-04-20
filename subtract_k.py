n = int(input("Enter a elements number: "))
arr =[int(input("Enters an element: ")) for j in range(n)]
k = int(input("Enter k number: "))
sorted_arr = sorted(arr)
count = 0
for i in arr:
    if i - k in sorted_arr:
        count += 1
print(count)