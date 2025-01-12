# 3. Write a python function named reconstruct_matrix that takes 
# decomposed matrixes ('U', 'S' and 'V') as parameters and returns 
# the original matrix using SVD techniques.  

import numpy as np

def reconstruct_matrix(U, S, V):
    return np.dot(U, np.dot(np.diag(S), V))

U = np.array([[1, 0], [0, 1]])
S = np.array([2, 3])
V = np.array([[1, 0], [0, 1]])
print("Rec matrix:", reconstruct_matrix(U, S, V))
