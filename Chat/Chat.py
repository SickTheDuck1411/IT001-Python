# Import
from Transmit import transmit
from GetData import GetData
# Function
# def Chat(DesId,port):
#     line=GetData()
#     print(line)
#     chat=str(input(""))
#     message=""
#     while line!="Bye"   or chat!=""     or line!=""     or  chat!="Bye":
#         message=message+chat
#         transmit(message,port)
#         message=""
#         line=GetData()
#         print(line)
#         chat=str(input(""))

def Chat(DesID, port) :
    line= GetData()
    print(str(line), end= "")
    while line != "Bye\n" and line:
        chat = str(input(""))
        if(chat == "Bye"): 
            break
        line = GetData()
        print(line, end= "")    


MyID="987654"
# main
Chat("1234567",80)