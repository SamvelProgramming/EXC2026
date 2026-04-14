# def fibonacci(num):
#     a = 1
#     b = 2
#     if num <= 0:
#         return -1
#     if num == 1:
#         return 1
#     for i in range(2, num):
#         a, b = b, a + b
#     return a

# num = int(input("Enter a number: "))
# print(fibonacci(num))

def fibonacci_n(num, a = 1, b = 2, pos = 2):
    if num <= 0:
        return -1
    if num == 1:
        return 1
    if b == num:
        return pos
    if b > num:
        return -1
    return fibonacci_n(num, b, a + b, pos + 1)

num = int(input("Enter a number: "))
print(fibonacci_n(num))