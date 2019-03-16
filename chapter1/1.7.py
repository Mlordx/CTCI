def setZero(matrix):
    N = len(matrix)
    M = len(matrix[0])
    
    
    matrix2 = []
    for i in range(N):
        matrix2.append([])
        for j in range(M):
            matrix2[i].append(matrix[i][j])

    for i in range(N):
        for j in range(M):
            if not matrix2[i][j]:
                for i2 in range(N): matrix[i2][j] = 0
                for j2 in range(M): matrix[i][j2] = 0

    return matrix


A = [[1,2,3,4],[5,6,0,2],[0,7,8,9]]

print(A)
print(setZero(A))
