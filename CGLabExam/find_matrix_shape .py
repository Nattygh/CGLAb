# 1. Write a python function named find_matrix_shape that can take 
# an matrix as a parameter and returns the shape of a matrix 
# def find_matrix_shape(matrix):
def find_matrix_shape(matrix):
    return len(matrix), len(matrix[0]) if matrix else 0

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Shape of the matrix:", find_matrix_shape(matrix))