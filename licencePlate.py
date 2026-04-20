licensePlate = "aBc 12c"
words = ["abccdef", "caaacab", "ccbaa", "abcdef", "aabbcc", "bacc"]
result = ""
for i in licensePlate.lower():
    if i.isalpha():
        result += i
for i in result:
    for j in words:
        if j.count(i) < result.count(i):
            words.remove(j)
shortest = min(words, key = len)
print(shortest)