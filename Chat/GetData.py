
file = open('Data.txt', "r")


def GetData():
    
    line =  file.readline()
    if not line :
        file.close()
    return line
