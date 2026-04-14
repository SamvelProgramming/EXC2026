# def factorial(num):
#     if num < 0:
#         return "Undefined"
#     if num < 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# num = int(input("Enter a number: "))
# print(factorial(num))

def factorial_n(num, pos = 1):
    if num < 0:
        return "Undefined"
    if num == 1:
        return pos - 1
    if num % pos != 0:
        return -1
    else:
        return factorial_n(num // pos, pos + 1)
    
num = 5040
print(factorial_n(num))

