def lights(n):
    light = n * [False]
    for i in range(1, n + 1):
        for j in range(n):
            if (j + 1) % i == 0:
                if light[j] is False:
                    light[j] = True
                else:
                    light[j] = False
    count = 0
    for i in light:
        if i is True:
            count += 1
            
    return count
print(lights(int(input("Enter a number: "))))