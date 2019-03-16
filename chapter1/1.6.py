from math import *


def rot(matrix):
    #N, M = matrix.shape
    N = len(matrix)
    M = len(matrix[0])
    
    if( N != M ): return -1

    for l in range(int(floor(N/2))):
        for i in range(l,N-l-1):
            temp = matrix[l][i]

            matrix[l][i] = matrix[N-i-1][l]

            matrix[N-i-1][l] = matrix[N-l-1][N-i-1]

            matrix[N-l-1][N-i-1] = matrix[i][N-l-1]

            matrix[i][N-l-1] = temp

    return matrix


A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(A)
print(rot(A))
                        
