from Manipulate import CreateArray, PrintArray

# Find Symmetry







# Main
a= CreateArray()
print(a)

reverse = []
# Reversed Array
for j in reversed (range(len(a))):
    reverse.append(a[j])    

print(reverse)
# Symmetry
listofsymmtry=[]
for i in range(len(a)): 
    for j in range(len(a)):
        if(a[i] == reverse[j]):
            step = 1
            while i+step < len(a) and j+step <len(a): 
                if (a[i+step] == reverse[j+step]):
                    step+=1
                else:
                    break 
            if  step!= 1:
                symmetricA=[]
                for k in range(0,step):
                    symmetricA.append(a[i+k])
                listofsymmtry.append(symmetricA)
list=[]
for symmetry in listofsymmtry:
    reverseSymmetry = []
    # Reversed Array
    for j in reversed (range(len(symmetry))):
        reverseSymmetry.append(symmetry[j])
    flag = True
    for m in range(0,len(symmetry)):
        if(symmetry[m] !=  reverseSymmetry[m]):
            flag= False
            break
    if(flag):
        list.append(symmetry)
print(list)

      
    