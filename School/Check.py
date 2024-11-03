import math
def sq(number):
    square = int(math.sqrt(number))
    if square*square==number:
        return True        
    return False
def prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if not(number % i) or i == 1  or i == 0: 
            return False
    return True 
checkprime = 0
arrprime = []
checksq = 0
arrsq = []
number = int(input("Enter your num"))
for i in range(0,number):
    if prime(i): 
        checkprime+=1  
        arrprime.append(i)
    elif sq(i):
        checksq+=1
        arrsq.append(i) 
print(checksq,checkprime)
print(arrsq,arrprime)