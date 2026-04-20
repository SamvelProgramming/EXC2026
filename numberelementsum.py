def summa(number):
    summ = 0
    number = abs(number)
    while number != 0:
        summ += number % 10
        number //= 10
    print(summ)


summa(int(input("Enter a number: ")))