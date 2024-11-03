# Vet Dau Loang
from Manipulate import PrintArray, CreateArray


class  Center: 
    def __init__(self,cs,ce):
        self.cs = cs
        self.ce= ce

# main
a = CreateArray()
PrintArray(a)




# Find Symmetry ( Oil Spilled )

for i in range(0,len(a)):

    if i< len(a)-2 and i< a[i] == a[i+2]:
        ce = i+1
        cs = i+1
        step = 1 
        while i+step < len(a) and i-step > 0:
            if a[i-step] == a[step+1]:
                step+=1
            else:
                break
        print(a[cs-step: ce+ step+1])

    elif i < len(a) -1 and a[i]== a[i+1]:
        ce = i 
        cs = i
        step = 1 
        while i+step < len(a) and i-step > 0:
            if a[i-step] == a[step+1]:
                step+=1
            else:
                break
        print(a[cs-step: ce + step+2])
            
