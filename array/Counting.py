a = [4,6,5,9,7,5,6,4,3,1,2,1,2,3,7,5,8]
j=[]
for i in range(1, len(a)):
    for x in range(0,len(a)-i):
        if a[x] > a[x+1]:
            temp=a[x+1]
            a[x+1]=a[x]
            a[x]=temp

print(len(a))

# j.append(a[0])
# for i in range(0,len(a)-1):
#     if a[i+1]==j[0]:
#         j.append(a[i+1])
#     else:
#         print(j[0],len(j))
#         j=[]
#         j.append(a[i+1])
# print(j[0],len(j))

value =a[0]
count = 1
for i in range(0,len(a)):
    if i == len(a) -1:
        print(value,count)
    elif  a[i+1] == value:
        count+=1
    else:
        print(value, count)
        value = a[i+1]
        count =1


          


