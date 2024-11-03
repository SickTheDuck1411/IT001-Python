# a = chr(66)
# print(a)
array = []
asciiConvert = []
for i in range(0 , 3):
    if i <= 1:
        asciiChar =  str(input("Enter your character: "))
        array.append(asciiChar)
        asciiConvert.append(ord(asciiChar))
    else:
        number = int(input("Enter your number: "))
        array.append(number)
        asciiConvert.append(chr(number))

print("Ma ascii cua ky tu",array[0], array[1],"lan luot la",asciiConvert[0],"va" , asciiConvert[1],"khoang cach giua hai ky tu la" , asciiConvert[1] - asciiConvert[0], "Dang viet hoa cua ky tu", array[0], "la", chr(asciiConvert[0]-32), array[2], "la ma ascii cu ky tu", asciiConvert[2])

