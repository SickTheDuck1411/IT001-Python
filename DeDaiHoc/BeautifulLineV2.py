def factorise(value):
    Factor = 0
    step = 0
    while value%2 == 0:
        value = value/2
        step+=1
    Factor = value
    return(step , Factor)

def removeOddElement(a):
    array = []
    for i in range(0,len(a)):
        if a[i] %2 == 0:
            array.append(a[i])
    return array

#Main
a = [40,6,40,3,20,1]
factorisedOddElements =[]
exponentalElemnts=[]
evenArray= removeOddElement(a)
for element in evenArray:
    result= factorise(element)
    if result[1] not in factorisedOddElements: 
        factorisedOddElements.append(result[1])
        exponentalElemnts.append(result[0])
    else: 
        for i,value in enumerate(factorisedOddElements):
            if(value == factorisedOddElements):
                if exponentalElemnts[i] < result[0]:
                    exponentalElemnts[i] = result[0]
            break




print(exponentalElemnts)
print(factorisedOddElements)
# Exponential = []
# for i in range(0,len(exponentalElemnts)):
#     highest = exponentalElemnts[i]
#     for j in range(0, len(exponentalElemnts)):
#         if factorisedOddElements[i] == factorisedOddElements[j]:
#             if exponentalElemnts[i] < exponentalElemnts[j]:
#                 highest = exponentalElemnts[j]
#     Exponential.append(highest)
# print(Exponential)


# oddNumbers=[]
# highestExponent=[]
# for i in range(0,len(factorisedOddElements)):
#     if factorisedOddElements[i] not in oddNumbers:
#         factorisedOddElement=factorisedOddElements[i]
#         exponentalElemnt= exponentalElemnts[i]
#         for j in range(i+1, len(factorisedOddElements)):
#             if factorisedOddElements[j] == factorisedOddElement and exponentalElemnt < exponentalElemnts[j] :
#                 exponentalElemnt= exponentalElemnts[j]
#         oddNumbers.append(factorisedOddElement)
#         highestExponent.append(exponentalElemnt)

# for element

# result= factorise(20)
# print(result)



# step = 0
# j=0

# element = int(input(" Type in how many elements for the line:  "))
# for i in range(0 ,element):
#     number = (int(input("Enter numbers for each element: ")))
#     a.append(number)
