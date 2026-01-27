def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()
    print()


matrix = []
size = int(input("Enter size: "))

for row in range(size):
    input_row = []
    print("Enter values: ")
    for value in range(size):
        input_row.append(int(input()))
    matrix.append(input_row)
print_matrix(matrix)

for index in range(size):
    temp = matrix[index][index]
    matrix[index][index] = matrix[index][size - index - 1]
    matrix[index][size - index - 1] = temp
print_matrix(matrix)
