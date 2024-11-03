def simplify(numerator,denominator):
    if denominator != 0:
        value = numerator
        remainder = denominator
        newremainder = (value%remainder)
        while newremainder !=0:
            value = remainder
            remainder = newremainder
            newremainder = value%remainder
        return remainder
    else:
        return False
a = simplify(-6,-4)
print(a)