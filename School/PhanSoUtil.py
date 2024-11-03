def simplify(numerator,denominator):
    value =numerator
    remainder = denominator
    newremainder = (value%remainder)
    while newremainder !=0:
        value = remainder
        remainder = newremainder
        newremainder = value%remainder
    return remainder
def bcnn(num1, num2):
    return int(num1*num2/simplify(num1, num2))
print(bcnn(6,8))