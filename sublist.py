def substring(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            if total == k:
                count += 1  
    return count


n = int(input("Enter an elements count: "))
nums = [int(input("Enter an element: ")) for i in range(n)]
k = int(input("Enter a k: "))
print(substring(nums, k))