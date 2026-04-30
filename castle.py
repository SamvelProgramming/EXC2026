def castle_drop(n):
    x = 0
    while (x * (x + 1)) // 2 < n:
        x += 1

    print(f"Minimum trials needed: {x}")

    current = 0
    step = x
    drops = []

    while current < n:
        current += step
        if current > n:
            drops.append(n)
        else:
            drops.append(current)
        step -= 1
        if step < 0:
            break

    print(f"Drop floors: {drops}")


n = int(input("Enter floors: "))
castle_drop(n)
