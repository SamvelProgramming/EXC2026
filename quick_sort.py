def quick_sort(arr):
    length = len(arr)

    if length <= 1:
        return arr
    else:
        pivot = arr.pop()

    greater_than_pivot = []
    less_than_pivot = []

    for i in arr:
        if i < pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


n = int(input("Enter the number of elements: "))
user_arr = [int(input(f"Enter an element {i + 1}: ")) for i in range(n)]
print(quick_sort(user_arr))
