from Manipulate import GenerateMatrix, printMatrix

# FindMin
def FindMin(matrix):
    min = matrix[0][0]
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] < min:
                min = matrix[i][j]
    return min


# Binh's Delivery
def Delivery(matrix, minimum):
    total=0
    for i in range (0,len(matrix)):
        for j in range(0,len(matrix[0])):
            total += matrix[i][j] - minimum
    return total


# Main
r = int(input("Input Row"))
c = int(input("Input Column"))
matrix = GenerateMatrix(r,c)
min = FindMin(matrix)
total = Delivery(matrix, min)
print(total)


