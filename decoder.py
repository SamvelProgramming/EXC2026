def count_decodings(message):
    if not message or message[0] == '0':
        return 0

    prev2 = 1
    prev1 = 1
    i = 1

    while i < len(message):
        count = 0
        if message[i] != '0':
            count = prev1

        two_digit = int(message[i - 1] + message[i])
        if 10 <= two_digit <= 26:
            count += prev2

        prev2 = prev1
        prev1 = count
        i += 1

    return prev1


try:
    message = input("Enter a code you would like to decode: ")
    print("Total ways:", count_decodings(message))
except:
    print("Please enter a valid code to decode!!!")
