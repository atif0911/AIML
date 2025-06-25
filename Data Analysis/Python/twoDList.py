#two dimensional list
matrix=[
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7],
    [4,5,6,7,8],
    [5,6,7,8,9]
]

print(matrix[2][3])

for row in matrix:
    for col in row:
        print(col)

for i in range(5):
    for j in range(5):
        print(matrix[i][j],"\t")
