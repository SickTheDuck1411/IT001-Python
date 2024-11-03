# arr = [2,5,9,1,6,0,34,4,3]

# for i in range(0,len(arr)):
#     minimum = arr[i]
#     for j in range(i+1, len(arr) ):
#         if arr[j]<minimum:
#             minimum = arr[j]

# print(arr)

# x,y =10,5
# print(x,y)
# x,y= y,x 
# print(x,y)                        

arr = [2,5,9,1,6,0,34,4,3]

for j in range(0,len(arr)-1):
    min = arr[j]
    position = j
    for i in range(j+1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            position = i
    arr[j] , arr[position] = min ,arr[j]


print(arr)