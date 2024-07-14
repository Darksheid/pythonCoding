

matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]

row1,col1,row2,col2 = [2, 1, 4, 3]
total = 0
for row in range(row1,row2+1):
    total = total + sum(matrix[row][col1:col2+1])
print(total)









