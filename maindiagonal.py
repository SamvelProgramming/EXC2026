matrix = [[1, 2, 3,],
          [4, 5, 6,],
          [7, 8, 9,]]
n = len(matrix)
upper_main = []
for i in range(n):
    for j in range(n):
        if j > i:
            upper_main.append(matrix[i][j])
print(upper_main)
if len(upper_main) == 0:
    print("the matrix contains one number or empty")
else:
    average = sum(upper_main) / len(upper_main)
    print(average)