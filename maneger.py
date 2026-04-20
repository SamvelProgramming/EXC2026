def find_first_false(product):
    for i, val in enumerate(product):
        if val is False:
            return i + 1
    return -1
product = [True, True, True, False, False, False]
print(find_first_false(product))