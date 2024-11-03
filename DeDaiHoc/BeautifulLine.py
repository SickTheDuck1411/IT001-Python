def removeValueArray(a, key):
    results= []
    for i in a:
        if i != key:
            results.append(i)
    value =key/2 
    if (value)%2 ==0 and (value) not in results:
        results.append(value)
    return results


def removeOddElement(a):
    array = []
    for i in range(0,len(a)):
        if a[i] %2 == 0:
            array.append(a[i])
    return array

def FindLargestEvenElement(a):
    largest = 0
    for i in range(0 , len(a)):
        if largest < a[i] and (a[i]%2) == 0:
            largest = a[i]
    return largest

def EnterArray():
    a = []
    element = int(input(" Type in how many elements for the line:  "))
    for i in range(0 ,element):
        number = (int(input("Enter numbers for each element: ")))
        a.append(number)
    return a



# Main
a=EnterArray()
a= removeOddElement(a) 

step = 0
while len(a) > 0:
    print(a)
    largest= FindLargestEvenElement(a)
    a= removeValueArray(a, largest)
    step+=1
print(step)


# print(step)



# print(largest)
# for i in range(0,element):
#     if a[i] == largest:
#         a.pop(i)
# print(a)        
# for i in range(0,element):
#     if largest == a[i]:
#        a[i] = a[i]/2 
#     # if a[i] % 2 == 0:
#     #     while j< element:
#     #         if a[j] == largest:
#     #             largest = largest/2
#     #             step+=1
#     #             j+=1
#     #         else:
#     #             a[j]= a[j] / 2
#     #             step+=1
#     #             j+=1
#     # j = 0
# print(a)
