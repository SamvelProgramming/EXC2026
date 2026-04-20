def multiplysimple(n):
    if n <= 1:
        return "Invalid"  
    total = 1
    for number in range(2, n+1):
        is_simple = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_simple = False
                break
        if is_simple:
            total *= number
    return total
print(multiplysimple(int(input("Enter a number: "))))