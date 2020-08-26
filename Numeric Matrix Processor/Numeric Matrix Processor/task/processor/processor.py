class MatricesOperations:

    def main_menu(self):
        while True:
            user_request = input("1. Add matrices\n"
                                 "2. Multiply matrix by a constant\n"
                                 "3. Multiply matrices\n"
                                 "4. Transpose matrix\n"
                                 "5. Calculate a determinant\n"
                                 "6. Inverse matrix\n"
                                 "0. Exit\n"
                                 "Your choice: ")
            if user_request == "1":
                self.addition()
            elif user_request == "2":
                self.multiply_by_constant()
            elif user_request == "3":
                self.multiply_by_matrices()
            elif user_request == "4":
                self.transpose_menu()
            elif user_request == "5":
                self.calculate_determinant()
            elif user_request == "6":
                self.inverse_matrix()
            elif user_request == "0":
                break
            else:
                print("Invalid Input")

    def get_matrix_int(self):
        matrix_dimension = input("Enter size of matrix: ").split(" ")
        matrix_dimension = [int(value) for value in matrix_dimension]
        matrix = []
        for i in range(matrix_dimension[0]):
            row_to_add = input().split(" ")
            row_to_add = [int(number) for number in row_to_add]
            matrix.append(row_to_add)
        return matrix_dimension, matrix

    def get_matrix_float(self):
        matrix_dimension = input("Enter size of matrix: ").split(" ")
        matrix_dimension = [int(value) for value in matrix_dimension]
        matrix = []
        for i in range(matrix_dimension[0]):
            row_to_add = input().split(" ")
            row_to_add = [float(number) for number in row_to_add]
            matrix.append(row_to_add)
        return matrix_dimension, matrix

    def addition(self):
        matrix_one_size, matrix_one = self.get_matrix_float()
        matrix_two_size, matrix_two = self.get_matrix_float()
        if self.can_add_matrices(matrix_one_size, matrix_two_size):
            self.sum_of_matrices(matrix_one, matrix_two)
        else:
            print("The operation cannot be performed.\n\n")

    def can_add_matrices(self, matrix_one_size, matrix_two_size):
        return matrix_one_size == matrix_two_size

    def sum_of_matrices(self, matrix_one, matrix_two):
        sum = []
        for i in range(len(matrix_one)):
            new_row = []
            for j in range(len(matrix_one[0])):
                new_row.append(matrix_one[i][j] + matrix_two[i][j])
            sum.append(new_row)
        print("The result is:\n")
        for i in range(len(sum)):
            for j in range(len(sum[0])):
                print(sum[i][j], end=" ")
            print()

    def multiply_by_constant(self):
        matrix_size, matrix = self.get_matrix_float()
        constant = float(input("Enter constant: "))
        self.multiplocation_by_constant(matrix_size, matrix, constant)

    def multiplocation_by_constant(self, matrix_size, matrix, constant):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] *= constant
        print("The result is:\n")
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print()

    def multiply_by_matrices(self):
        matrix_one_size, matrix_one = self.get_matrix_float()
        matrix_two_size, matrix_two = self.get_matrix_float()
        if matrix_one_size[1] == matrix_two_size[0]:
            result = self.new_matrix_multiplication(matrix_one_size, matrix_two_size)
            for i in range(matrix_one_size[0]):
                for j in range(matrix_two_size[1]):
                    new_value = 0
                    for ii in range(matrix_one_size[1]):
                        new_value += matrix_one[i][ii] * matrix_two[ii][j]
                    result[i][j] = new_value
            print("The result is:\n")
            for i in range(len(result)):
                for j in range(len(result[0])):
                    print(result[i][j], end=" ")
                print()
        else:
            print("The operation cannot be performed.\n\n")

    def new_matrix_multiplication(self, matrix_one_size, matrix_two_size):
        matrix = [[] for i in range(matrix_one_size[0])]
        for i in range(matrix_one_size[0]):
            matrix[i] = [[] for i in range(matrix_two_size[1])]
        return matrix

    def transpose_menu(self):
        user_request = input("1. Main diagonal\n"
                             "2. Side diagonal\n"
                             "3. Vertical line\n"
                             "4. Horizontal line\n"
                             "Your choice: ")
        matrix_size, matrix = self.get_matrix_float()
        if user_request == "1":
            self.transpose_main_diagonal(matrix_size, matrix)
        elif user_request == "2":
            self.transpose_side_diagonal(matrix_size, matrix)
        elif user_request == "3":
            self.transpose_vertical_line(matrix)
        elif user_request == "4":
            self.transpose_horizontal_line(matrix_size, matrix)
        else:
            print("Invalid Input")

    def transpose_main_diagonal(self, matrix_size, matrix):
        matrix_transposed = self.new_matrix(matrix_size)
        for i in range(matrix_size[1]):
            for k in range(matrix_size[0]):
                matrix_transposed[k][i] = matrix[i][k]
        print("The result is:\n")
        for i in range(len(matrix_transposed)):
            for j in range(len(matrix_transposed[0])):
                print(matrix_transposed[i][j], end=" ")
            print()

    def transpose_side_diagonal(self, matrix_size, matrix):
        if matrix_size[0] != matrix_size[1]:
            matrix_size.reverse()
        matrix_transposed = self.new_matrix(matrix_size)
        for i in range(matrix_size[1]):
            for k in range(matrix_size[0]):
                matrix_transposed[k][i] = matrix[i][k]
        matrix_transposed.reverse()
        for i in range(len(matrix_transposed)):
            matrix_transposed[i].reverse()
        print("The result is:\n")
        for i in range(len(matrix_transposed)):
            for j in range(len(matrix_transposed[0])):
                print(matrix_transposed[i][j], end=" ")
            print()

    def transpose_vertical_line(self, matrix):
        matrix_transposed = matrix
        for i in range(len(matrix_transposed)):
            matrix_transposed[i].reverse()
        print("The result is:\n")
        for i in range(len(matrix_transposed)):
            for j in range(len(matrix_transposed[0])):
                print(matrix_transposed[i][j], end=" ")
            print()

    def transpose_horizontal_line(self, matrix_size, matrix):
        matrix_transposed = matrix
        matrix.reverse()
        print(matrix_transposed)
        print("The result is:\n")
        for i in range(len(matrix_transposed)):
            for j in range(len(matrix_transposed[0])):
                print(matrix_transposed[i][j], end=" ")
            print()

    def new_matrix(self, matrix_size):
        if matrix_size[0] != matrix_size[1]:
            matrix_size.reverse()
        matrix = [[] for i in range(matrix_size[0])]
        for i in range(matrix_size[0]):
            matrix[i] = [[] for i in range(matrix_size[1])]
        return matrix

    def calculate_determinant(self):
        matrix_size, matrix = self.get_matrix_float()
        matrix_determinant = self.determinant(matrix)
        print("The result is:\n")
        print(matrix_determinant)
        print()

    def matrix_minor(self, matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

    def determinant(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = 0
        for i in range(len(matrix)):
            determinant += ((-1) ** i) * matrix[0][i] * self.determinant(self.matrix_minor(matrix, 0, i))
        return determinant

    def inverse_matrix(self):
        matrix_size, matrix = self.get_matrix_float()
        matrix_determinant = self.determinant(matrix)
        if matrix_size[0] != matrix_size[1] or matrix_determinant == 0:
            print("This matrix doesn't have an inverse.")
        else:
            if len(matrix) == 2:
                return [[matrix[1][1] / matrix_determinant, -1 * matrix[0][1] / matrix_determinant],
                        [-1 * matrix[1][0] / matrix_determinant, matrix[0][0] / matrix_determinant]]

                # find matrix of cofactors
            cofactors = []
            for r in range(len(matrix)):
                cofactor_row = []
                for c in range(len(matrix)):
                    minor = self.matrix_minor(matrix, r, c)
                    cofactor_row.append(((-1) ** (r + c)) * self.determinant(minor))
                cofactors.append(cofactor_row)
            cofactors = self.transpose_inverse(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = round(cofactors[r][c] / matrix_determinant, 3)
            print("The result is:\n")
            for i in range(len(cofactors)):
                for j in range(len(cofactors[0])):
                    print(cofactors[i][j], end=" ")
                print()
            print()

    def transpose_inverse(self, matrix):
        matrix_transposed = self.new_matrix([len(matrix), len(matrix[0])])
        for i in range(len(matrix[0])):
            for k in range(len(matrix)):
                matrix_transposed[k][i] = matrix[i][k]
        return matrix_transposed





run_system = MatricesOperations()
run_system.main_menu()

"""
matrix_one_dimension = input().split(" ")
matrix_one_dimension = [int(value) for value in matrix_one_dimension]

matrix_one = []
for i in range(matrix_one_dimension[0]):
    row_to_add = input().split(" ")
    row_to_add = [int(number) for number in row_to_add]
    matrix_one.append(row_to_add)

constant = int(input())

for i in range(len(matrix_one)):
    for j in range(len(matrix_one[0])):
        matrix_one[i][j] *= constant
for i in range(len(matrix_one)):
    for j in range(len(matrix_one[0])):
        print(matrix_one[i][j], end=" ")
    print()


matrix_two_dimension = input().split(" ")
matrix_two_dimension = [int(value) for value in matrix_two_dimension]

matrix_two = []
for i in range(matrix_two_dimension[0]):
    row_to_add = input().split(" ")
    row_to_add = [int(number) for number in row_to_add]
    matrix_two.append(row_to_add)


if matrix_one_dimension == matrix_two_dimension:
    sum_of_matrices = []
    for i in range(len(matrix_one)):
        new_row = []
        for j in range(len(matrix_one[0])):
            new_row.append(matrix_one[i][j] + matrix_two[i][j])
        sum_of_matrices.append(new_row)
    for i in range(len(sum_of_matrices)):
        for j in range(len(sum_of_matrices[0])):
            print(sum_of_matrices[i][j], end=" ")
        print()

else:
    print("ERROR")
"""
