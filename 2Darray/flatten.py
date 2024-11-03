from ManipulateMatrix import GenerateMatrix, printMatrix

# column   major

def flattenByColumnMajor(matrix):
    array=[]
    for i in range(0,len(matrix[0])):
        for j in range(0,len(matrix)):
            a=matrix[j][i]
            array.append(a)
    return array

# row major
def flattenByRowMajor(matrix):
    array=[]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            a=matrix[i][j]   
            array.append(a)
    return array

def printArray(resultedArray):
    for i in resultedArray:
        print(i,end=" ")



# Main
matrix = GenerateMatrix(4,4)
printMatrix(matrix)
