n = int(input("Enter a number: "))
saved = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
if rev == saved:
    print("Your number is palindrome")
else:
    print("No your number is not palindrome")