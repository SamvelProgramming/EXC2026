words = ["Hello", "Alaska", "Dad"]
row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"
result = []
for word in words:
    first = 0
    second = 0
    third = 0
    check = word.lower()
    for i in check:
        if i in row1:
            first += 1
        elif i in row2:
            second += 1
        elif i in row3:
            third += 1
    if first == len(word) or second == len(word) or third == len(word):
        result.append(word)
print(result)