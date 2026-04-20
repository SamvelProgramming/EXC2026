elements = int(input("Enter elements number: "))
arr = [int(input(f"Enter element {i}: ")) for i in range(elements)]
n = int(input("Enter which biggest number you want: "))
arr_set = set(arr)
if n > len(arr_set):
    print("Not enough numbers")
else:
    for i in range(n - 1):
        arr_set.remove(max(arr_set))
    print("Result:", max(arr_set))