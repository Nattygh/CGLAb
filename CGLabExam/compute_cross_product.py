# 2. Write a python function named compute_cross_product that can 
# take two arrays as a parameter and return the cross product of the 
# arrays.

import numpy as np

def compute_cross_product(array1, array2):
    return np.cross(array1, array2)

array1 = [1, 2, 3]
array2 = [4, 5, 6]
print("Cross product:", compute_cross_product(array1, array2))