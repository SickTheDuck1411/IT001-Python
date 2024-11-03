import numpy as np

def ScanRow(row) :
    missedNumber=[1,2,3,4,5,6,7,8,9]
    for i in row:
        if i !=0:
            missedNumber.remove(i) 
    return missedNumber


def ScanColumn(sudoku, indexOfColumn) :
    missedNumber=[1,2,3,4,5,6,7,8,9]
    for i in range(0,len(sudoku)):
        if sudoku[i][indexOfColumn] !=0:
            missedNumber.remove(sudoku[i][indexOfColumn])
    return missedNumber
    # for i in column:
    #     if i !=0:
    #         missedNumber.remove(i) 
    # return missedNumber





# 
sudoku = [[5,4,3,9,2,1,8,7,6],
          [2,1,9,6,8,7,5,4,3],
          [8,7,6,3,5,4,2,1,9],
          [9,8,7,4,0,5,3,2,1],
          [3,2,1,7,9,8,6,5,4],
          [6,5,4,1,0,2,9,8,7],
          [7,6,5,2,4,3,1,9,8],
          [4,3,2,8,1,9,7,6,5],
          [1,9,8,5,7,6,4,3,2]]
# num = [1,2,3,4,5,6,7,8,9]
# num1 = [1,2,3,4,5,6,7,8,9]
# result = sudoku
# array = []

# for i in range(0,len(sudoku)):
#     for j in range(0,len(sudoku)):
#         if sudoku[i][j] == 0:
#             positionY = i
#             positionX = j
#             for x in range(0,len(sudoku)):
#                 if sudoku[positionY][x] in num:
#                     num.remove(sudoku[positionY][x])
#             for y in range(0,len(sudoku)):
#                 if sudoku[y][positionX] in num1:
#                     num1.remove(sudoku[y][positionX])
#             array.append(num1)
    
row = len(sudoku)
column= len(sudoku[0])
missPositions = []

for i in range(0,row):
    for j in range(0, column): 
        if sudoku[i][j] ==0:
            missPositions.append((i,j))

print(missPositions)

print(ScanRow(sudoku[3]))
print(ScanColumn(sudoku, 4))
# 
while(len(missPositions)!=0):
    for (i,position) in enumerate(missPositions):
        rowPosition = position[0]
        columnPosition= position[1]
        rowMissedNumber = ScanRow(sudoku[rowPosition])
        columnMissedNumber = ScanColumn(sudoku,columnPosition)
        if len(rowMissedNumber) ==1 :
            sudoku[rowPosition][columnPosition] = rowMissedNumber[0]
            missPositions.pop(i)
            break
        elif len(columnMissedNumber) == 1:
            sudoku[rowPosition][columnPosition] = columnMissedNumber[0]
            missPositions.pop(i)
            break
            
print(sudoku)

# for i in range(0,len(sudoku)):
#     for j in range(0,len(sudoku)):
#         if sudoku[i][j] == 0:
#             positionY = i
#             positionX = j
#             for x in range(0,len(sudoku)):
#                 if sudoku[positionY][x] in num:
#                     num.remove(sudoku[positionY][x])
#             for y in range(0,len(sudoku)):
#                 if sudoku[y][positionX] in num1:
#                     num1.remove(sudoku[y][positionX])
#             array.append(num1)
# print(array)
# for i in range(0,len(sudoku)):
#     for j in range(0,len(sudoku)):
#         if sudoku[i][j] == 0:
#             positionY = i
#             positionX = j
#             for x in range(0,len(sudoku)):

#                 if sudoku[positionY][x] == array[0][1] :
#                     result[positionY][positionX]=array[0][0]
#                     break
#                 elif sudoku[positionY][x] == array[0][0] :
#                     result[positionY][positionX]=array[0][1]
#                     break
#             print( result[positionY][positionX])
# for i in result:
#     print(i)               
# print(array)                   
# print(sudoku)
