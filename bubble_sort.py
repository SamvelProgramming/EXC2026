def bubble_sort(arr):
    length = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, length):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter an element {i + 1}: ")) for i in range(n)]
print(bubble_sort(arr))
