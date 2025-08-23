import numpy as np

def split_matrix(matrix):
    n = matrix.shape[0]
    mid = n // 2
    a11 = matrix[:mid, :mid]
    a12 = matrix[:mid, mid:]
    a21 = matrix[mid:, :mid]
    a22 = matrix[mid:, mid:]
    return a11, a12, a21, a22

def strassen(a,b):
    if a.shape[0] == 1:
        return a*b
    
    a11, a12, a21, a22=split_matrix(a)
    b11, b12, b21, b22=split_matrix(b)
     
    p1 = strassen(a11, b12-b22)  
    p2 = strassen(a11+a12, b22) 
    p3 = strassen(a21+a22, b11) 
    p4 = strassen(a22, b21-b11) 
    p5 = strassen(a11+a22, b11+b22) 
    p6 = strassen(a12-a22, b21+b22) 
    p7 = strassen(a11-a21, b11+b12) 
    
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7
    
    top = np.hstack((c11, c12))
    bottom = np.hstack((c21, c22))
    c = np.vstack((top, bottom))
    return c


a = np.array([[1, 2, 3, 1],
             [4, 0, 1, 2],
             [2, 1, 0, 3],
             [3, 4, 2, 1]])

b = np.array([[2, 1, 0, 3],
              [1, 3, 4, 2],
              [0, 2, 1, 5],
              [4, 1, 2, 0]])

f = strassen(a,b)
print(f)
