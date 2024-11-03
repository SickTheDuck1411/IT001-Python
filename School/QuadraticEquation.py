import math
a = int(input("Enter your number: ")) 
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
print(f'{a}x*x+{b}x+{c}')
delta = b*b - (4*a*c)

if delta > 0:
    x1 = ((b*b) + math.sqrt(delta))/(2*a)
    x2 = ((b*b) - math.sqrt(delta))/(2*a)
    print("phan thư thứ shai ")
    print(x1,x2)
elif delta == 0:
    x1 = -(b/2*a)
    print(x1)
else: 
    print("Not found")

