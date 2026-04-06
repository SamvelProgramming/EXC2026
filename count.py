def count(nums):
    lst = []
    for i in nums:
        if i in lst:
            return True
        lst.append(i)
    return False

n = int(input("Enter a number: "))
nums = [int(input("Enter a number: ")) for i in range(n)]
print(count(nums))
# def count(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# n = int(input("Enter the number of elements: "))
# nums = [int(input("Enter a number: ")) for _ in range(n)]
# print(count(nums))