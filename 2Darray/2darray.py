
def print2d(matrix):
    for i in range (0,len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")






# matrix=[]


# for i in range(0,3):
#     a=[]
#     for j in range(0,5):
#         a.append(i*10+j)
#     matrix.append(a)

# input matrix value from keyboard
# matrix=[]
# for i in range(0,3):
#     a=[]
#     for j in range(0,2):
#         a.append(int(input(":")))
#     matrix.append(a)






# matrix=[]
# for i in range(0,4):
#     a=[]
#     for j in range(0,3):
#         a.append(i*10+j)
#     matrix.append(a)
# import random
# def randomMatrix():
#     matrix=[]
#     r = random.randrange(3,5)
#     c= random.randrange(3,5)
#     for i in range(0,r):
#         a=[]
#         for j in range(0,c):
#             a.append(i*10+j)
#         matrix.append(a)
#     return matrix;    

        
# matrix = [[1,2,3],[4,5],[8,9,10]]

# for i in range(0, len(matrix)):
#     for j in range(0,len(matrix[i])):
#         print(matrix[i][j],end=" ")
#     print("")



# print2d(matrix)

# for i in range(0,len(matrix)):

# for i in range(0,4):
#     for j in range(0,3):
#         print(matrix[i][j], end=" ")
#     print("")

# matrix=[]

# for i in range(0,4): 
#     matrix.append([])

# for i in range(0,3):
#     for j in range(0,4):
#         matrix[j].append(input(""))
        
# print2d(matrix)

# matrixabc=[[1,2,3],[4,5,6],[7,8,9]]
# matrix=[]

# for i in range(0,3):
#     matrix.append([])

# for i in range(0,3):
#     for j in range(0,3):
#         matrix[j].append(matrixabc[i][j])
# print2d(matrix)

import numpy 
matrix =numpy.zeros((3,5), dtype=int)
# count=1
# n=4
# for i in range(0,3):
#     matrix[i][0]=count
#     count+=1
#     for j in range(0,5):
#         matrix[i][j]=n
#         n+=1

# count =1
# for i in range(0,3):
#     for j in range(0,5):
#         matrix[i][j]=count
#         count+=1

count =1
for j in range(0,5):
    for i in range(0,3):
        matrix[i][j]=count
        count+=1

transportMatrix =numpy.zeros((5,3), dtype=int)

for i in range(0,3):
    for j in range(0,5):
        transportMatrix[j][i]= matrix[i][j]


print2d(transportMatrix)



