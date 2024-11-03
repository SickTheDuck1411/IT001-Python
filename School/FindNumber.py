import random
number = random.randrange(0,200)
arrayrand = []
# # numOfArray = 1
# arrayrand.append(number)
# status = True
# arrayrand.append(number)
# for i in range(1,5):
#     while status:
#         randnum = random.randrange(0,200)
#         if randnum not in arrayrand:
#             status = True
#             arrayrand.append(randnum)
#             break
#         else:
#             status=False
# print(arrayrand)

# realarray= []
# similiar = arrayrand[0]
# realarray.append(similiar)           
# for i in range(1,len(arrayrand)):
#     if arrayrand[i]!= similiar:
#         similiar = arrayrand[i]
#         realarray.append(similiar)

# print(realarray)
i=0
while i < 5:
    randnum = random.randrange(0,200)
    if randnum not in arrayrand:
        arrayrand.append(randnum)
        i+=1
print(arrayrand) 
