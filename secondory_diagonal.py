matrix = [[1, 2, 3,],
          [4, 5, 6,],
          [7, 8, 9,]]
n = len(matrix)
under_secondary = []
for i in range(n):
    for j in range(n):
        if i + j > n - 1:
            under_secondary.append(matrix[i][j])

print(under_secondary) # this will prinnt the list of numbers there are under secondary diagonal which are 6, 8, 9
average = sum(under_secondary) / len(under_secondary)
print(average) 
print("։")