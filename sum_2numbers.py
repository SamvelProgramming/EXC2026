def sum_of_two(num1, num2):
    lst1 = list(num1[::-1])
    lst2 = list(num2[::-1])
    result = []
    carry = 0
    max_len = max(len(lst1), len(lst2))
    while len(lst1) < max_len:
        lst1.append('0')
    while len(lst2) < max_len:
        lst2.append('0')
    for i in range(max_len):
        digit_sum = int(lst1[i]) + int(lst2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
    if carry:
        result.append(str(carry))

    return "".join(result[::-1])
num1 = "1111111111111111111111111111111111111111111111111111111111111111111111"
num2 = "9999999999999999999999999999999999999999999999999999999999999999999999"
print("Sum:", sum_of_two(num1, num2))