def quick_sort(lst):
    length = len(lst)

    if length <= 1:
        return lst
    else:
        pivot = lst.pop()

    greater_than_pivot = []
    less_than_pivot = []

    for i in lst:
        if i < pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def binary_search(arr, target):
    length = len(arr)
    start_index = 0
    end_index = length - 1

    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return "Your target is on the list!!!"
        elif mid_val < target:
            start_index = mid + 1
        else:
            end_index = mid - 1

    return "Sorry your target is out of the list"


n = int(input("Enter the number of elements: "))
user_input = [int(input(f"Enter an element {i + 1}: ")) for i in range(n)]
sorted_list = quick_sort(user_input)
target = int(input("Enter a number you are looking for: "))
print(binary_search(sorted_list, target))
