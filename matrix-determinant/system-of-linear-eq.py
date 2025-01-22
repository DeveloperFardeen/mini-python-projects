import numpy as np

def get_coefficients_matrix(n):
    """Get the coefficient matrix from the user."""
    coefficients = []
    print(f"Enter the coefficients of the {n} equations row by row (space-separated):")
    for i in range(n):
        row = input(f"Equation {i + 1}: ").strip().split()
        if len(row) != n:
            print(f"Error: Equation {i + 1} must have exactly {n} coefficients. Please re-enter.")
            return get_coefficients_matrix(n)
        coefficients.append([float(x) for x in row])
    return coefficients

def get_constants_vector(n):
    """Get the constants vector from the user."""
    print(f"Enter the constant terms for the {n} equations (space-separated):")
    constants = input().strip().split()
    if len(constants) != n:
        print("Error: The number of constants must match the number of equations. Please re-enter.")
        return get_constants_vector(n)
    return [float(x) for x in constants]

# Main Program
print("Solve a System of Linear Equations (Ax = b)")
n = int(input("Enter the number of variables (n): "))
if n < 1:
    print("Number of variables must be at least 1.")
else:
    A = get_coefficients_matrix(n)  # Coefficients matrix
    b = get_constants_vector(n)    # Constants vector
    
    print("\nCoefficient Matrix (A):")
    for row in A:
        print(" ".join(map(str, row)))
    
    print("\nConstants Vector (b):")
    print(" ".join(map(str, b)))
    
    # Solve the system of equations
    try:
        A = np.array(A)
        b = np.array(b)
        x = np.linalg.solve(A, b)  # Solve Ax = b
        print("\nSolution (x):")
        for i, val in enumerate(x, 1):
            print(f"x{i} = {val:.2f}")
    except np.linalg.LinAlgError:
        print("\nError: The system of equations has no unique solution (matrix is singular or not invertible).")
