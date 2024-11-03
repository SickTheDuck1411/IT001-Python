
# lenNumber = int(input("Type in your length of numbers:"))
# array = []
# arrayCentrePosition = []
# for i in range(0, lenNumber ):
#     number = int(input("Type in each of your number: "))
#     array.append(number)


# def findcentre(lennum):
#     findcentre = 0
#     if lennum % 2 != 0:
#         findcentre = int(lennum/2)
#         arrayCentrePosition.append(findcentre)
#     else:
#         for i in range(0,2):
#             findcentre = int(lennum/2)-1+ i 
#             arrayCentrePosition.append(findcentre)
# centre = findcentre( lenNumber)
# print(arrayCentrePosition)

# #function
# def FindCentre(lenNumber):
#     arrayCentrePosition=[] 
#     if lenNumber % 2 != 0:
#         arrayCentrePosition.append(int(lenNumber/2))
#     else:
#         arrayCentrePosition.append(int(lenNumber/2)-1)
#         arrayCentrePosition.append(int(lenNumber/2))
#     return arrayCentrePosition


# def FindTotalError(array,lenNumber, centrePostion):
#     totalError = 0
#     if lenNumber % 2 != 0: 
#         # so le
#         for i in range(1, centrePostion[0]+1):
#             if array [centrePostion[0]-i] != array[centrePostion[0]+i]:
#                 totalError+=1
        
#     else:
#         #so chan         
#         for i in range(0,centrePostion[0]+1):
#             if array[centrePostion[0] - i] != array[centrePostion[1] + i]:
#                 totalError+=1
#     return totalError

# #Main 
# lenNumber = int(input("Type in your length of numbers:"))
# array = []
# for i in range(0, lenNumber ):
#     number = int(input("Type in each of your number : "))
#     array.append(number)

# centrePostion= FindCentre(lenNumber)
# numberofError= FindTotalError(array, lenNumber, centrePostion) 
# if numberofError <= 1:
#     print(True)
# else:
#     print(False)

# Attempt 2
# Def
def CreateArray():
    array = []
    lengtthOfArray = 0
    lengtthOfArray = int(input("Type in how many elements in your array: "))
    for i in range(0,lengtthOfArray):
        array.append(int(input("Enter your number in the array: ")))
    return array, lengtthOfArray


def CountTotalError(array , lengthOfArray):
    totalError = 0
    for i in range(0,int(lengthOfArray / 2)):
        if array[i] != array [lengthOfArray - i -1]:
            totalError += 1

    return totalError



# Main
(array, lengthOfArray) = CreateArray()
TotalError = CountTotalError(array , lengthOfArray )



if TotalError <= 1:
    print(True)
else:
    print(False)