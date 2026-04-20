nums = [100, 4, 200, 1, 3, 2]
num_set = set(nums)
longest = 0
for i in nums:
    if i - 1 not in num_set:
        current = i
        length = 1
        while current + 1 in num_set:
            current += 1
            length += 1
        longest = max(longest, length)
print(f"Longest consecutive sequence length is: {longest}")