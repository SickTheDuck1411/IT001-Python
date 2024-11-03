import numpy
def GenerateMatrix(r,c):
    matrix= numpy.zeros((r,c),dtype = int)
    count=1
    for i in range(0,r):
        for j in range(0,c):
            matrix[i][j]= count
            count+=1
    return matrix
def printMatrix(matrix):
    for i in range (0,len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")

