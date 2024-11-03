    # def
def Getstart(startposition):
    space = startposition - 1
    total = 0
    for i in range (0 , len(words)):
        if words[i] == " ":
            total +=1
        elif total == space:
            return i
    return -1

    
def GetWord(total):
    fnString = ""
    if total != -1:
        for i in range(total,len(words)):
            fnString = fnString + words[i]
            if words[i] == " ":
                break
    return fnString

def IgnoreWord(ignore):
    ignoreList = ['for', 'and' , 'of' , 'to' , 'the']
    LowerIgnore = ignore.lower()
    ignoreWord= LowerIgnore.strip()
    for element in ignoreList:
        if element == ignoreWord: 
            return True
    return False

def GetInitials():
    initialWord=''
    numofspace = 0
    for element in words:
        if element ==' ':
            numofspace+=1
    numofword = numofspace+1
    for i in range(0,numofword):
        position = Getstart(i+1)
        word= GetWord(position)
        if not IgnoreWord(word):
            initialWord+= word[0]
    return initialWord
# main
words = str(input("Enter the full name: "))
print(GetInitials())
# startposition = int(input("Enter your start point: "))
# position = Getstart(startposition)
# ignore = ("Enter your ignore word: ")
# ignore = GetWord(position)      
# print(IgnoreWord(ignore))