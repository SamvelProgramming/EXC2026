def repetitions(nums, k):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    result = []
    while len(result) < k:
        max_num = None
        max_count = -1
        for num in count:
            if count[num] > max_count and num not in result:
                max_count = count[num]
                max_num = num
        result.append(max_num)
    return result
# case1
nums = [1, 1, 1, 2, 2, 3]
k = 2
# case2
# nums = [1]
# k = 1
# case3
# nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
# k = 2
print(repetitions(nums, k))