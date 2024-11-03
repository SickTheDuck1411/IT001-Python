import numpy
def printMatrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j],end=" ")
        print("")
        
matrix = numpy.zeros((3,5), dtype=int)

# matrix[2][1]= 9
# for i in range(0, len(matrix)):
#     for j in range(0,len(matrix[i])):
#         matrix[i][j]= int(input(""))


# for i in range(0,5):
#     for j in range(0, len(matrix)):
#         matrix[j][i]= int(input(""))


print("hello world")
printMatrix(matrix)