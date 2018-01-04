# Matrix Algebra

import numpy as np

# Given matrices:

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([[6, 2, -3, 5]])
v = np.array([[3, 5, -1, 4]])
w = np.array([[1], [8], [0], [5]])

# 1. Matrix Dimensions

np.shape(A) # (2, 3)
np.shape(B) # (2, 2)
np.shape(C) # (3, 2)
np.shape(D) # (2, 3)
np.shape(u) # (1, 4)
np.shape(w) # (4, 1)

# 2. Vector Operations

u + v # [9, 7, -4, 9]
u - v # [3, -3, -2, 1]
6 * u # [36, 12, -18, 30]
np.dot(u,v.T) # 51
np.linalg.norm(u) # 8.6023

# 3. Matrix Operations

A + C # does not exist
A - C.T # [[-4, -7, -3], [3, 6, 4]]
C.T + 3 * D #[[14, 3, 3], [2, 7, 9]]
B.dot(A) # [[-1, -5, -1], [2, 7, 4]]
B.dot(A.T) # does not exist
B.dot(C) # does not exist
C.dot(B) # [[5, -6], [9, -8], [6, -6]]
B.dot(B).dot(B).dot(B) # [[1, -4], [0, 1]]
A.dot(A.T) # [[14, 28], [28, 69]]
D.T.dot(D) # [[10, -4, 0], [-4, 8, 8], [0, 8, 10]]