number = int(input("Input your number: "))
Power = 0
Multiply = 1
MultiplySum=0
Divide = 1
DivideSum = 0
element = 1
for i in range(1, number+1):
    Power = Power + pow(i , i)
    Multiply = Multiply*i
    MultiplySum += Multiply
    Divide = 2/(i*(i+1))
    DivideSum += Divide

                   



        

print(Power , MultiplySum, DivideSum)
