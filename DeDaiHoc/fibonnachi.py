
# number = int(input("Number of times for looping in fibonnachi:"))
# if(number<=2) : 
#     print(1)
#     exit()
# a= [1,1]
# for i in range(2, number):
#     a.append(a[i-1]+ a[i-2])


# lenofArray= len(a)

# print(a[lenofArray-1])        

# f1 = 1
# f2 = 1
# total = 0
# numOfIterate = number - 2
# for i in range(0, numOfIterate):
#     total = f1 + f2
#     f1 = f2
#     f2 = total   
# print(total)



#def
# def fibonanci(number): 
#     if number <=2:
#         return 1
#     return fibonanci(number-1) + fibonanci(number-2)

#Main
# number = int(input("Number of times for looping in fibonnachi:"))
# print(fibonanci(number))





# def(factorial)
def factorial(number):
    if number <=1:
        return 1
    return number * factorial(number - 1)




# main
basenum = int(input("Which number you want to input: "))
print(factorial(basenum))