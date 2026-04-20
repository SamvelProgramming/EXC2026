def armstrong(degree):
    lst = []
    if degree < 15:
        for i in range(1, 10 ** degree):
            summa = 0
            copy = i
            while copy != 0:
                digit = copy % 10
                summa += digit ** degree
                copy //= 10
            if summa == i and len(str(i)) == degree:
                lst.append(i)
        return lst
    else:
        return "Pls enter degree below 15"
print(armstrong(int(input("Enter a degree: "))))