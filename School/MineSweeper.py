import numpy as np
# def


# Main
array = [[0,1,0,0],
         [1,0,0,1],
         [0,0,0,0],
         [0,1,1,1]]
newArray = []
row = len(array)
column = len(array[0])
result = np.zeros((row, column), dtype= int)
# newArray = []
# for i in range(0,len(array[0])):
#     number = 0
#     for j in range(0,len(array[0])):
for i in range(0,row):
    if i == 0:
        # Dong dau
        for j in range(0,column):
            if j == 0:
                result[i][j] = array[i][j+1]+  array[i+1][j]
            elif j== column-1:
                result[i][j] = array[i][j-1]+  array[i+1][j]
            else:
                result[i][j] = array[i][j-1]+  array[i+1][j]+  array[i][j+1]

    elif i == row - 1:
        #  DONG CUOI
        for j in range(0,column):
            if j == 0:
                result[i][j] = array[i-1][j]+array[i][j+1]
                print(result[i][j])
            elif j== column - 1:
                result[i][j] = array[i][j-1]+array[i-1][j]
            else:
                result[i][j] = array[i][j-1]+array[i-1][j]+array[i][j+1]
    else: 
        for j in range(0,column):
            if j==0:
                result[i][j]=array[i-1][j]+array[i][j+1]+array[i+1][j]
            elif j== column-1:
                result[i][j]= array[i][j-1]+array[i+1][j]+array[i-1][j]
            else:
                 result[i][j]= array[i-1][j]+array[i][j-1]+array[i][j+1]+array[i+1][j]
print(result)



