import numpy as np

def get_matrix_input(title):
    print(title)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1} values separated by spaces: ").split()))
        if len(row) != cols:
            raise ValueError("Number of columns does not match the input")
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix, name):
    print(f"{name}:\n{matrix}")

def main():
    # Input matrices
    matrix1 = get_matrix_input("Enter the first matrix:")
    matrix2 = get_matrix_input("Enter the second matrix:")

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose of matrix")

    operation = input("Enter the number of the operation: ")

    if operation == '1':
        if matrix1.shape != matrix2.shape:
            print("Matrices must be of the same shape for addition.")
        else:
            result = matrix1 + matrix2
            print_matrix(result, "Result of Addition")

    elif operation == '2':
        if matrix1.shape != matrix2.shape:
            print("Matrices must be of the same shape for subtraction.")
        else:
            result = matrix1 - matrix2
            print_matrix(result, "Result of Subtraction")

    elif operation == '3':
        if matrix1.shape[1] != matrix2.shape[0]:
            print("Number of columns of the first matrix must be equal to number of rows of the second matrix for multiplication.")
        else:
            result = np.dot(matrix1, matrix2)
            print_matrix(result, "Result of Multiplication")

    elif operation == '4':
        print("Transpose of the first matrix:")
        print_matrix(matrix1.T, "First Matrix Transpose")
        print("Transpose of the second matrix:")
        print_matrix(matrix2.T, "Second Matrix Transpose")

    else:
        print("Invalid operation")

main()

