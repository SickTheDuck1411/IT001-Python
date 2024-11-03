from GetData import GetData



# huong dan su dung GetData()
line = GetData()
while line: 
    print(line)
    line = GetData()



# Khai bao ham
def ReceiveFile(filename):
    
    file = open(filename,"w")
    count=0
    line=GetData()
    while line !="****":
        count += len(line)
        file.write(line)
        line = GetData()
    print(f'{count} characters were written to {filename}')
    file.close()
# Main
ReceiveFile("newfile.txt")