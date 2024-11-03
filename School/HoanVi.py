import numpy as np
#def
def Amount(n):
    total = 1
    for i in reversed(range(1,n+1)):
        total = total*i
    return total
# def AutoTest(n, result):
#     length = Amount(n)
#     if length != len(result):
#         return False
#     for i in range (0,length):
#         for k in range (i+1,length):
#             if(result[i]== result[k]):
#                 print(result[i], result[j])
#                 return False 
#     return True
# def Amount(n):
#     if(n < 1): return 1
#     return n*Amount(n-1) 


#main
n = int(input("Enter number of permuation"))    
# xu ly case 1 
if(n==1): 
    print([1])
    exit()
# xu ly case khac 1
lengthofPermutation= Amount(n)
result = []
# count = 0
# substitute = (n-1)
# position = 0
# checking = 0
# increment = 0
for i in range(0,lengthofPermutation):
    result.append([1])     


# if (n!=2):
#     while count < lengthofPermutation and substitute <= n:
        
#         if position < n:
            
#             result[count].insert(position,substitute)
#             count+=1
#             position+=1
#         elif count == lengthofPermutation:
#             count = 0
#             position = 0
#             substitute+=1 
#         else:
#             result[count].insert(position,substitute)
#             count+=1
#             position-=1
for i  in range(2,n+1):
    k = 0
    for j in range(0, lengthofPermutation):
        if k == i : k=0
        result[j].insert(k,i)
        k+=1

# result[0].insert(0,2)
# result[1].insert(1,2)
# result[2].insert(0,2)
# result[3].insert(1,2)
# result[4].insert(0,2)
# result[5].insert(1,2)

# result[0].insert(0,3)
# result[1].insert(1,3)
# result[2].insert(2,3)
# result[3].insert(0,3)
# result[4].insert(1,3)
# result[5].insert(2,3)


# print(AutoTest(n,result))

# index = 0
# for i in range(0,n):
#     for j  in range(0,int(lengthofPermutation/2)):
#         result[index].insert(i,2)
#         index+=1        
# if (n == 2):
#     result.append(n,n-1)
#     result.append(n-1,n)
print(result)



