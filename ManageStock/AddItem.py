from OnlyAlpha import *;
newFile=open("NewStock.txt","w")
# khai bao ham
def AddItem(item):
    if  CheckInfo(item)==True:
        newFile.write(f'{item}\n')     

# tao  file with nam NewStock.txt# 
# sau do checkinfo neeus valid thi additem to file newStock.txt
#Main


items=[
"1234XTEaasdf",
"1235YOIaasdf",
"1236XTEaasdf",
"1237YFGaasdf",
"1238YURaasdf",
"9999THUdsaf",
"12236tredasfd"
]





for i in range(0,len(items)):
    item=items[i]
    AddItem(item)
