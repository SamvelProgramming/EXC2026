def target_nums(nums, target):
    arr = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                arr.append(i)
                arr.append(j)
                return arr
target = 6
nums = [3, 3, 4]
print(target_nums(nums, target))