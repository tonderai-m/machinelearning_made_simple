
def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):   
        new_row = [] 
        for row in matrix:
            new_row.append(row[i])  # This packages separate list of [x0[i],x1[i],x2[i],x3[i]]
        transposed.append(new_row)

    return transposed


def matrix_multiply(A, B):
    # This function multiplies matrices A and B

    # Initialize sizes
    rows_A = len(A)
    cols_A = len(A[0])
    
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Number of A columns must be equal to number of B rows for matrix multiplication")
    
    # initialize the matrix stucture with zeroes to compute sum += for dot product adding the multiplications saving to memory
    result = []
    for i in range(rows_A):
        result.append([0] * cols_B)    

    # Matrix multiplication dot product
    for i in range(rows_A):
        for j in range(cols_B):
            sum = 0
            for k in range(cols_A):  # or for k in range(rows_B)
                sum += A[i][k] * B[k][j]
            result[i][j] = sum

    return result
