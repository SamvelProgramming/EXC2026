def substring(text):
    lst = []
    j = 0
    while text[j] not in lst:
        for i in text:
            if i in lst:
                j += 1
                lst.clear()
                break
            lst.append(i)
            j += 1
        return len(lst)
text = input("Enter a string: ")
print(substring(text))
