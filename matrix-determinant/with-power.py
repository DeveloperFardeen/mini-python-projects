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

def calculate_matrix_power(matrix, power):
    """Calculate the power of the matrix using numpy."""
    return np.linalg.matrix_power(matrix, power)

# Main program
n = int(input("Enter the size of the matrix (n x n): "))
if n < 1:
    print("Matrix size must be at least 1.")
else:
    matrix = get_matrix_input(n)
    print("\nMatrix:")
    for row in matrix:
        print(" ".join(map(str, row)))
    
    # Calculate determinant
    determinant = calculate_determinant(matrix)
    print(f"\nThe determinant of the given {n}x{n} matrix is: {determinant}")
    
    # Ask for matrix power
    power = int(input("\nEnter the power to which the matrix should be raised: "))
    powered_matrix = calculate_matrix_power(np.array(matrix), power)
    
    print(f"\nThe matrix raised to the power of {power} is:")
    for row in powered_matrix:
        print(" ".join(map(str, row)))
