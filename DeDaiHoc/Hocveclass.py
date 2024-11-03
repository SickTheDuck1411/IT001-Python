#def


class StringOveride:
    def __init__(self,value):
        self.value= value

    def lowercaseOveride(self):
        words= self.value    
        results= "" 
        for char in words:
            asciiChar = ord(char)
            if asciiChar <=90 and asciiChar >=65:
                asciiChar= asciiChar + 32
            results+= chr(asciiChar)
        resultedClass= StringOveride(results)
        return resultedClass

    def uppercaseOveride(self):
        words= self.value    
        results= "" 
        for char in words:
            asciiChar = ord(char)
            if asciiChar <=90 + 32 and asciiChar >=65 + 32:
                asciiChar= asciiChar - 32
            results+= chr(asciiChar)
        resultedClass= StringOveride(results)
        return resultedClass
#Main


words = StringOveride("Tuyen Nguyen TrAn TRonG")
lowerWords= words.lowercaseOveride()
upperWords = lowerWords.uppercaseOveride()
print(upperWords)
# print(words.lower())



# words= "Tuyen Nguyen TrAn TRonG"
# lowerWords= words.lower()
# upperWord = lowerWords.upper()
# print(upperWord)
# #
# UpperCase = []
# LowerCase = []
# i = 65
# j = 97
# while i<91:
#     UpperCase.append(chr(i))
#     i+=1

# while j<123:
#     LowerCase.append(chr(j))
#     j+=1

# print(LowerCase)
# print(UpperCase)



# for char in words:
#     for i in range(0, len(UpperCase)):
#         if char in UpperCase:
#             Lower = LowerCase[i+32]
    

# lower case 
# identify  upper case 
# lower case
