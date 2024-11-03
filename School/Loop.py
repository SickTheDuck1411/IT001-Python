array = []
NoOfarray = int(input("Enter No of array: "))
for i in range(0,NoOfarray):
    array.append(int(input("Enter your number: ")))
# min = array[0]
# Minlocation = 0
# max = array[NoOfarray-1]
# Maxlocation = NoOfarray-1

# for i in range(0,len(array)):
#     if array[i]<min:
#         min = array[i]
#         Minlocation = i:

# for i in reversed(range(0,len(array))):
#     if array[i]> max:
#         max = array[i]
#         Maxlocation = i

min = max = array[0]
minLocation= maxLocation =0
# for (i,value) in enumerate(array):
#     if value > max: 
#         max= value
#         maxLocation= i
#     if value < min : 
#         min= value
#         minLocation= ij
for i in range(0, NoOfarray):
    if array[i] > max: 
        max= array[i]
        maxLocation= i
    if array[i] < min : 
        min= array[i]
        minLocation= i

print(max,maxLocation)
print(min,minLocation)

