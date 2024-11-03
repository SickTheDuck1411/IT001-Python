#def
def CreateArray(): 
    array = []
    lenghtOfArray = int(input("Enter your number want to contain in the array: "))
    if lenghtOfArray == 0: exit()
    for i in range(0,lenghtOfArray):
        array.append(int(input("Type in your number:")))
    return array
def FindSmallestNumberandAppearance(array):         
    count = 0
    smallest = array[0]
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]

    for i in range(0,len(array)):
        if smallest== array[i]:
            count+=1 
    return (smallest, count)
def findSmallestNumberandAppearanceV2(array):
    total = 0
    smallest = array[0]
    for i in range(0,len(array)):
        if array[i] < smallest:
            smallest = array[i]
            total = 1 
        elif array[i]  == smallest:
            total+=1
    return total , smallest

#Main 
array = CreateArray()
(count, smallestnumber) = findSmallestNumberandAppearanceV2(array)
print(count , smallestnumber)
# print(smallest , count)
# (smallest, count) = FindSmallestNumberandAppearance(array)

