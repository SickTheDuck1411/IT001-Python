import numpy
count=1
matrix=numpy.zeros((3,5),dtype=int)
for j in range(0,5):
    for i in range(0,3):
        matrix[i][j]=count
        count+=1


# for i in range(0,3):
#     for j in range(0,5):
#         print(matrix[i][j],end=" ")
#     print("")

# print(matrix)

# for i in reversed(range(0,3)):
#     print(i)

# total=0
# for i in range(0,3):
#     for j in range(0,5):
#         total=total+matrix[i][j]
# print(total)

# def transposeMatrix(matrix): 
    
#     matrix1= numpy.zeros((len(matrix[0]),len(matrix)), dtype=int)
#     for i in range(0,5):
#         for j in range(0,3):
#             matrix1[i][j]=matrix[j][i]

#     return matrix1
# tranpose = transposeMatrix(matrix)

# print(tranpose)
# print(matrix)
# total=0
# count=1
# for i in range(0,len(matrix)):
#     for j in range(0,len(matrix[i])):
#         total=total+matrix[i][j]
#     print("hang",count,"=",total)
#     total=0
#     count+=1




# def calculateRow(matrix):
#     results=[]
#     total =0
#     for i in range(0,len(matrix)):
#         for j in range(0, len(matrix[i])):
#             total+= matrix[i][j]
#         results.append(total)
#         total=0
#     return results




# rowResults = calculateRow(matrix)


# for i in range(0,len(rowResults)):
#     print(f'Row {i+1}: {rowResults[i]}' )
# total =0
# for i in range(0,len(rowResults)):
#     total+= rowResults[i]
# print(total) 



