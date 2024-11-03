arr = []
for i in range(0,4):
    arr.append(int(input("Enter your number: ")))
[num1,num2,num3,num4] = arr

denominator = arr[1] * arr[3]
numerator1 = arr[0] * arr[3]
numerator2 = arr[2 ] * arr[1]

numerator = numerator1+ numerator2
if denominator < numerator:
    newarr = [denominator,numerator]
else:
    newarr = [numerator,denominator]
print(newarr)
# print(num1, num2, num3, num4)

