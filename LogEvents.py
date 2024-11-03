

LogArray = ["ray" ,"fa","fdsw","Empty" , "fdsa","fsd","cxv", "asd" , "a", "sfsa" ,"Empty"  ,  "sfdaf", "sdafd","vx","asfw" , "sdafa" ,"Empty" , "Empty", "end"]

flag = True
def LogEvent( LogArray ):
    file = open("LogFile.txt",'a')
    for i in range (0 , len (LogArray)):
        if LogArray[i ] != "Empty":
            file.write(f'{LogArray[i]}\n')
    file.close()
Log = LogEvent(LogArray)
print(Log)
