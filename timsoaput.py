# import random
# array =[8,3,1,0,5,6,12,43,32,5,234,432,456,1,0,23,4567,341,634,643,645,76,3456,223,4356,0]
# x = len(array)
# index=[]
# ut=0 
# aput=0
# if array[0] > array[1]:
#     ut= array[1]
#     aput= array[0]
# else: 
#     ut= array[0]
#     aput= array[1] 

# n=2
# while n<x: 
#     if(array[n]< ut): 
#         aput = ut
#         ut = array[n]
#         index=[]
#         index.append(n)
#     elif(array[n]< aput  and array[n]!= ut ):
#         aput = array[n]
#         index=[]
#         index.append(n)
#     elif array[n]== aput:
#         index.append(n)
#     n =n+1
# print("aput",aput)
# for k in range(0,len(index)):
#     print(index[k])
