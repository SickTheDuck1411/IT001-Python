#def
def insert(i, j):
    if not  (i <= len(arr)-1 and j<i and j > 0 ): return False
    
    # temp = arr[j]

    # arr[j] = arr[i]
    # arr[i] = temp
    # for i in range(j,i):
    #     if arr[i] < arr[j]:

    # print(arr)
    temp = arr[i]
    for k in reversed(range(j,i)):
        arr[k+1]= arr[k]
    arr[j]= temp 
    print(arr)
    
# def printb(arr1):
#     print(arr1[1])

# def printa():
#     arr1=[1,2,3,4]
#     printb(arr1)
#Main
arr = [7,6,-1,5,3,4,2]
insert(3,-3)
print(arr)


# for i in range(1,len(arr)):
#     for j in range(0,i):
#         if arr[i]<arr[j]:
#             insert(i, j)
#             break
# print(arr)
