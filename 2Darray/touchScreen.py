import numpy

from ManipulateMatrix import printMatrix


# Function
def SetRow(RowNum,NumSkip,NumPixel):
    # for i in range(0,RowNum):
    #     for j in range(0,NumSkip):
    #         screenMatrix[i][j+Set]=1
    for i in range(NumSkip,NumSkip+NumPixel):
        screenMatrix[RowNum][i]=1
def SearchInRow(RowNum,StartCol, screenMatrix):
    if RowNum > len(screenMatrix):
        print("Out Of Range")
        return -1

    if StartCol==1:
        for i in screenMatrix[RowNum]:
            if i==1:
                return i
    elif StartCol==20:
        for i in reversed(screenMatrix[RowNum]):
            if i == 1:
                return i
    
    return -1            


# Main
# Define ScreenMatrix
screenMatrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0] , [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0] ,[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0] , [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
# screenMatrix= numpy.zeros((10,20),dtype=int)
RowNum=int(input(":"))
# NumSkip=int(input(":"))
# NumPixel=int(input(":"))

if RowNum <= len(screenMatrix): 
    StartCol = int(input("Either 1 or 20: "))    
    print(SearchInRow(RowNum,StartCol,screenMatrix))
else:
    print("Out Of Range")
    
# SetRow(RowNum,NumSkip,NumPixel)
# print(screenMatrix[3])

printMatrix(screenMatrix)






        