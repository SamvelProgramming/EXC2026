aliceSizes = [2, 4]
bobSizes = [1, 2, 5]
while sum(aliceSizes) != sum(bobSizes):
    if sum(aliceSizes) > sum(bobSizes):
        item = aliceSizes.pop(0)
        bobSizes.append(item)
    else:
        item = bobSizes.pop(0)
        aliceSizes.append(item)
    print(aliceSizes)
    print(bobSizes)