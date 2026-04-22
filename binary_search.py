def binary_search(arr, target):
    def search(low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return search(low, mid - 1)
        return search(mid + 1, high)

    return search(0, len(arr) - 1)
elements_count = int(input("Enter an elements count: "))
nums = [int(input(f"Element number {i + 1}: ")) for i in range(elements_count)]
number = int(input("Enter a number you would like to found: "))
print(binary_search(nums, number))