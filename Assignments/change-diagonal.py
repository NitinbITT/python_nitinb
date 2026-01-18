def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print()
    print()

matrix=[]
size=int(input("Enter size: "))
value=0

for i in range(size):
    row=[]
    for j in range(size):
        row.append(value)
        value+=1
    matrix.append(row)
print_matrix(matrix)

for i in range(size):
    temp=matrix[i][i]
    matrix[i][i]=matrix[i][size-i-1]
    matrix[i][size-i-1]=temp
print_matrix(matrix)