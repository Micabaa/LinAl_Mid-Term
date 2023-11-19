def main():
    matrix = get_square_matrix()
    inverse = inverse_matix(matrix)
    print_inverse(inverse)
    solve_system_option(matrix)
   

##############################


# Asks the user to enter a square matrix of any size.
# It then appends the values to the variable matrix as a list.
# If the input is the wrong number of elements, it raises an error.
def get_square_matrix():
    n = int(input("Enter the size of the square matrix: "))
    matrix = []
    for i in range(n):
        row_input = input(f"Enter row {i + 1} (space seperated values): ")

        # Converts a space-separated string of numbers
        # into a list of floating-point values, representing a row of a matrix.
        row = [float(x) for x in row_input.split()]
        
        if len(row) != n:
            raise ValueError(f"Row {i + 1} should have {n} elements.")
        matrix.append(row)
    return matrix


# Checks first if the matrix is square.
# If not, it calculates the inverse.
def inverse_matix(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Input matrix must be square.")
    
    augmented_matrix = [row + [int(i == j) for j in range(n)] for i, row in enumerate(matrix)]

    # Performs Gauss-Jordan elimination
    for col in range(n):

        # Finds the pivot row
        pivot_row = col
        max_value = abs(augmented_matrix[col][col])
        for i in range(col + 1, n):
            current_value = abs(augmented_matrix[i][col])
            if current_value > max_value:
                max_value = current_value
                pivot_row = i

        try:
            # Checks for a zero pivot value
            if augmented_matrix[pivot_row][col] == 0:
                raise ZeroDivisionError("Error: The matrix is singular and does not have an inverse.")

            # Wwaps the current row with the pivot row
            augmented_matrix[col], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[col]

            # Scales the pivot row to make the pivot element 1
            pivot_value = augmented_matrix[col][col]
            augmented_matrix[col] = [elem / pivot_value for elem in augmented_matrix[col]]

            # Eliminates other rows
            for row in range(n):
                if row != col:
                    factor = augmented_matrix[row][col]
                    augmented_matrix[row] = [elem - factor * augmented_matrix[col][i] for i, elem in enumerate(augmented_matrix[row])]

        except ZeroDivisionError:
            return None

    # Extracts the inverse matrix from the augmented matrix
    inverse = [row[n:] for row in augmented_matrix]
    return inverse


# Checks and prints the inverse matrix.
# If it does not exist, it raises an error.
def print_inverse(inverse):
    if inverse is not None:
        print("Inverse matrix:")
        for row in inverse:
            print(row)
    else:
        print("Error: The matrix is singular and does not have an inverse.")


# Asks the user wether they want to solve a linear equation system.
# If yes, it asks the user to enter a right-hand side vector b
# and calls the solve_linear_system function
def solve_system_option(matrix):
    solve_system = input("Do you want to solve a linear equation system? (y/n): ")
    if solve_system.lower() == 'y':
        b_input = input("Enter the right-hand side vector b (space separated values): ")
        b = [float(x) for x in b_input.split()]
        solve_linear_system(matrix, b)


# Solves a system of linear equations Ax = b and prints the solution.
# If the matrix is singular, it prints an error message.
# It uses the inverse and multiplies it with the entered vector b.
# So that x = A^(-1)b.
def solve_linear_system(matrix, b):
    inverse = inverse_matix(matrix)
    if inverse is not None:
        transposed_inverse = [list(row) for row in zip(*inverse)]

        # To solve the multiplication, the function involves iterating over
        # the rows of 'b' and columns of the transposed inverse matrix 'A^-1'.
        # For each element in the resulting matrix, perform element-wise multiplication 
        # of the corresponding elements from the row of 'b' and column of 'A^-1', 
        # and then sum these products to obtain the corresponding element of the solution vector.
        # The outer list comprehension iterates over each row in 'b', 
        # and the inner list comprehension constructs the elements of the solution vector 'x'.
        solution = [sum(ai * bi for ai, bi in zip(row, b)) for row in inverse]
        print("Solution of the linear equation system Ax = b:")
        for value in solution:
            print(value)
        return solution  # Return the solution vector
    else:
        print("Error: The matrix is singular and does not have an inverse.")
        return None

        
if __name__ == "__main__":
    main()