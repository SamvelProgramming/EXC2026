def rle(text):
    seen = {}
    result = []
    for i in text:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1
    for i,j in seen.items():
        if j > 1:
            result.append(f"{j}{i}")
        else:
            result.append(i)
    return "".join(result)
text = "aabbbcd"
print(rle(text))