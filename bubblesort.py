# unsortArray= [3,2,34,1,65,7,45,2,4,6]
# for k in range(0, len(unsortArray)-1):
#     for i in range(0,len(unsortArray) - k-1 ):
#         if unsortArray[i] > unsortArray[i+1] : 
#             temp = unsortArray[i]
#             unsortArray[i]= unsortArray[i+1]s
#             unsortArray[i+1] = temp
# print(unsortArray)


 
# Global 2D array 

arrayunsort = [[120,121,122,123,124,125,126,127,128,129],
               [3,   6,  8,  6,  4,  8,  2,  1,  5,  8]]

numOfCandidate = len(arrayunsort[0]) 
# print(len(arrayunsort[0]), len(arrayunsort[0]))
# print(arrayunsort[1][0])

# for i in range(0, len(arrayunsort)-1):
#     for j in range(0, len(arrayunsort) - i - 1):
#         if arrayunsort[1][j] > arrayunsort[1][j+1]:
#             arrayunsort[1][j+1] = temp
#             arrayunsort[1][j+1] = arrayunsort   [1][ j]
#             arrayunsort[1][j] = temp

for i in range(0, numOfCandidate-1):
    for j in range(0, numOfCandidate-i-1):
        if arrayunsort[1][j] > arrayunsort[1][j+1]:
            temp =   arrayunsort[1][j]
            arrayunsort[1][j] = arrayunsort[1][j+1]
            arrayunsort[1][j+1] = temp 

            temp =   arrayunsort[0][j]
            arrayunsort[0][j] =arrayunsort[0][j+1]
            arrayunsort[0][j+1] = temp 

# print(len(arrayunsort))

# print(arrayunsort)

print(arrayunsort)


















# sort = arrayunsort[1]


# for i in range ( 0 , len(sort) - 1) :
#     for j in range(0 , len(sort) - i-1):
#         if sort[j] > sort[j+1]:
#             temp = sort[j+1]
#             sort [j+1] = sort[j]
#             sort [j] = temp
# arrayunsort[1] = sort
# print( arrayunsort)
# # for i in range ( 0 , len(arrayunsort) - 1) :
# #     for j in range(0 , len(arrayunsort) - i-1):
# #         if arrayunsort [j]> arrayunsort[j+1]:
# #             temp2 = arrayunsort[j+1]
# #             arrayunsort[j+1] = arrayunsort [j]
# #             arrayunsort[j] = temp2

