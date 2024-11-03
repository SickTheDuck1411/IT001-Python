# number = int(input("Input your number:"))
# array=[]
# total=0
# for i in range(0,number):
#     variable = int(input("input your number:"))
#     array.append(variable)
#     while len(array)>=number:
#         for m in range(0,number):
#             for j in range(0,number):
#                 if j != m:
#                     total=array[m]+array[j]
#             j=0
# print(total)        
            




#def function
def ArrayInput(noa):
    a=[] 
    for i in range(0,noa): 
        x = int(input(f'Enter the {i+1} st number: '))
        a.append(x)
    return a

def calculateResult(arrayofint): 
    total=0 
    for i in range(0,noa): 
        for j in range(i+1,noa):
            total += arrayofint[i]*arrayofint[j]
    return total


#Main 
#Input 
noa= int(input("Enter the number of array: "))
a= ArrayInput(noa)

#Calculate
total= calculateResult(a)

print(total%100)


                