import numpy as np

def get_matrix_input(n):
    """Function to get matrix input from the user."""
    matrix = []
    print(f"Enter the elements of the {n}x{n} matrix row by row (space-separated):")
    for i in range(n):
        row = input(f"Row {i + 1}: ").strip().split()
        if len(row) != n:
            print(f"Error: Row {i + 1} must have exactly {n} numbers. Please re-enter.")
            return get_matrix_input(n)
        matrix.append([float(x) for x in row])
    return matrix

def calculate_determinant(matrix):
    """Calculate the determinant of the matrix using numpy."""
    return round(np.linalg.det(matrix), 2)

# Main program
n = int(input("Enter the size of the matrix (n x n): "))
if n < 1:
    print("Matrix size must be at least 1.")
else:
    matrix = get_matrix_input(n)
    print("\nMatrix:")
    for row in matrix:
        print(" ".join(map(str, row)))
    
    determinant = calculate_determinant(matrix)
    print(f"\nThe determinant of the given {n}x{n} matrix is: {determinant}")
