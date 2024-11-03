# array = [9,3,4,1,2,5,1,0]
# # bubble sort
# for i in range(0,len(array)):
#     for j in range(0,len(array)-i-1):
#         if array[j]>array[j+1]:
#             array[j],array[j+1]=array[j+1],array[j]
# print(array)
# linear
# number = int(input("Enter your num: "))
# for i in range(0,len(array)):
#     count = i
#     if array[i]==number:
#         print("found at",count)
# binary
# ub = len(array)-1
# lb = 0 
# number = int(input(":"))
# while lb<=ub:
#     mid = int((ub+lb)/2)
#     if array[mid] == number:
#         print(mid)
#         break
#     elif lb==ub:
#         print(array[lb])
#         if array[lb] == number: print(lb)                                               
#         else:  print("not found")
#         break
#     else:
#         if array[mid]<number:
#             lb=mid+1
#         else:
#             ub=mid-1
# Insertion sort
array = [4,5,6,1,2,3,7,6,1]
for i in  range(0,len(array)):
    key = array[i]
    j = i-1
    while key<array[j] and j>=0:
        array[j+1]=array[j]
        j-=1
    array[j+1]=key
print(array)

