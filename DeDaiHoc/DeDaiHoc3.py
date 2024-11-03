# DefFunction








# MAIN
candle = int(input("Input number of candle:"))
# khonloi= candle

# for i in range(0,candle):
#     wax=i
#     candle=0

# for i in range(0, wax):
#     if i % 2 ==0:
#         candle+=1
#     elif wax % 2 != 0:
#         wax=1 
# total=0
# extrawax=0
# if candle != 0:
#     while candle !=0:
#         candle -=1
#         wax+=1
#         total+=1
#         if wax % 2 == 0:
#             candle += 1
#     if wax % 2 != 0:
#         total+=1
# print(total + khonloi)          


while candle > 0:
    wax+= candle
    total+=candle
    candle = int(wax / 2)
    wax= wax%2
print(total)    


    