n = int(input("Enter elements count: "))
arr = [int(input("Enter element: ")) for i in range(n)]
if arr == sorted(arr) or arr[::-1] == sorted(arr):
    print("Yes")
else:
    swap = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if arr == sorted(arr):
                swap = 1
            arr[i], arr[j] = arr[j], arr[i]
    if swap == 1:
        print("Yes")
    else:
        print("No")