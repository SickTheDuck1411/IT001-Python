import numpy
def GenerateMatrix(r,c):
    matrix= numpy.zeros((r,c),dtype = int)
    for i in range(0,r):
        for j in range(0,c):
            matrix[i][j]= int(input(":"))
    return matrix
def printMatrix(matrix):
    for i in range (0,len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")

def CreateArray():
    a=[]
    numofarray= int(input("Enter the number of array: "))
    for i in range(numofarray):
        a.append(int(input(':')))    
    return a

def PrintArray(a):
    for i in a :
        print(i, end=' ')
    print("")
    