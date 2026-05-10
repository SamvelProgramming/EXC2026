def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0 
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

n = int(input("Enter a count of elements: "))
list1 = [int(input(f"Enter an element {i + 1}: ")) for i in range(n)]
list2 = [int(input(f"Enter an element {i + 1}: ")) for i in range(n)]
print(merge_sorted_lists(list1, list2))