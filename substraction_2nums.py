def subtract_two(num1, num2):
    if num1 == num2:
        return "0"

    negative = False
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        num1, num2 = num2, num1
        negative = True

    lst1 = list(num1[::-1])
    lst2 = list(num2[::-1])
    result = []
    borrow = 0

    max_len = max(len(lst1), len(lst2))

    while len(lst1) < max_len:
        lst1.append('0')
    while len(lst2) < max_len:
        lst2.append('0')

    for i in range(max_len):
        digit1 = int(lst1[i]) - borrow
        digit2 = int(lst2[i])

        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0

        result.append(str(digit1 - digit2))

    while len(result) > 1 and result[-1] == '0':
        result.pop()

    res = "".join(result[::-1])
    if negative:
        return "-" + res
    return res


num1 = "10000000000000000000000000000000000000000000000000"
num2 = "9999999999999999999999999999999999999999999999999"
print(subtract_two(num1, num2))