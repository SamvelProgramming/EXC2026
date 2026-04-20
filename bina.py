def bina(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_b > len_a:
        return False
    for i in range(len_a):
        isTrue = True
        for j in range(len_b):
            if a[i] != b[j]:
                isTrue = False
                print(a[i], b[j])
                break
            else:
                i += 1
        if isTrue:
            return True
    return False
a = input("Enter a text: ")
b = input("Enter another text: ")
print(bina(a, b))
