# Khai bao ham -> luu vao memory
def OnlyAlpha(string):
    return string.isalpha()

def CheckInfo(line):
    if OnlyAlpha(line[4:7])!=True:
        return False
    if int(line[0:4])>5999 or  int(line[0:4])<1:
        return False
    return True


#Main
# file=open("Stock.txt","r")
# for line in file.readlines():
#     print(CheckInfo(line))