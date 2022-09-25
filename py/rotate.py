# original matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
for row in matrix:  
    print(row)

print("\n")
# now zip it
matrix = list(zip(*matrix))
for row in matrix:  
    print(row)

print("\n")
# now rotate it 90 degrees conter clockwise
matrix = list(reversed(matrix))
for row in matrix:  
    print(row)
