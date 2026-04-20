def stick_count(arr):
    n = len(arr)
    for i in range(n):
        if len(arr) == 0:
            break
        print(len(arr))
        shortest = min(arr)
        for j in range(len(arr)):
            arr[j] -= shortest   
        new_arr = []
        for x in arr:
            if x > 0:
                new_arr.append(x)
        arr = new_arr
n = int(input("Enter an elements count: "))
arr = [int(input(f"Enter an element: "))for i in range(n)]
stick_count(arr)