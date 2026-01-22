def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()
    print()


matrix = []
size = int(input("Enter size: "))

for row in range(size):
    inputRow = []
    print("Enter values: ")
    for value in range(size):
        inputRow.append(int(input()))
    matrix.append(inputRow)
print_matrix(matrix)

for index in range(size):
    temp = matrix[index][index]
    matrix[index][index] = matrix[index][size - index - 1]
    matrix[index][size - index - 1] = temp
print_matrix(matrix)
