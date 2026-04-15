def convert(number, base1, base2):
    decimal = 0
    power = 0
    for digit in number[::-1]:
        d = int(digit)
        if d >= base1:
            return "Invalid"
        decimal += d * (base1 ** power)
        power += 1

    if decimal == 0:
        return "0"
        
    result = []
    while decimal > 0:
        result.append(str(decimal % base2))
        decimal //= base2
        
    return "".join(result[::-1])

number = input("Enter a number: ")
base1 = int(input("Enter a base1: "))
base2 = int(input("Enter "))
print(convert("12", 1, 1))