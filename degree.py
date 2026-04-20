# def degree(m, n):
#     return n ** m
# print(degree(int(input("Enter a number: ")), int(input("Enter a number: "))))
def degree(m, n,):
    a = 1
    while n > 0:
       a *= m
       n -= 1
    return a
print(degree(int(input("Enter a number: ")), int(input("Enter a degree: "))))