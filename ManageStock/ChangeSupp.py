# file = open("Stock.txt", "r")
# # count =0
# # for line in file.readlines():
# #     count+=1
# #     print(line)
# # print(count)
# file.close()

# names = ["John", "Alice", "Bob"]

# file = open("names.txt", "a")
# # for name in names:
# #     file.write(name + "\n")
# for i in range(0, len(names)):
#     file.write(names[i]+"\n")
# file.close()

# input XTE
# new file with XTE-> ABC

  
file = open("Stock.txt", "r")
for line in file.readlines():
    print(line)
file.close
file  = open("newStock.txt","w")

Code1 = "XTE"
Code2= "ABC"
file= open("Stock.txt","r")
newfile= open("NewStock.txt","w")

for line in file.readlines():
    newText=line
    if line[4:7]==Code1:
        newText=line.replace(Code1, Code2)
    newfile.write(newText)
file.close()
newfile.close()
