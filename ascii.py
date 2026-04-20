ascii = int(input("Enter a code: "))
method = 0
ascii = str(ascii)
if int(ascii[0]) == 0 or (int(ascii[0]) > 2 and int(ascii[1]) == 0):
    print(0)
else:
    for i in range(len(ascii)):
        if i + 1 < len(ascii):
            if int(ascii[i + 1]) != 0 and int(ascii[i]) <= 2 and int(ascii[i]) + int(ascii[i + 1]) <= 26:
                method += 2
            elif int(ascii[i + 1]) != 0 and int(ascii[i]) < 2 and int(ascii[i]) + int(ascii[i + 1]) <= 26:
                method += 1
    print(method)