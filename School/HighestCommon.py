# array = [15,20]
# if array[1]>array[0]:
#     value = array[1]
#     remainder = array[0]
# else:
#     value = array[0]
#     remainder = array[1]
# # while True:
# #       temp = value
# #       value = remainder
# #       remainder = temp%value
# #       if remainder == 0:
# #          break
# # print(array[0]/value,"/",array[1]/value)

def Euclid(num1,num2):
#     # if num2>num1:
#     #     remainder = num1
#     #     value = num2
#     # else:
#     #     value = num1
#     #     remainder = num2
#     # cach 2
    value = num2 if num2>num1 else num1
    remainder = num1 if num2> num1 else num2
    #cach 3
    # (value, remainder) = (num2,num1)

    while True:
        temp = value
        value = remainder
        remainder = temp%value
        if remainder == 0:
            break
    result = f'{int(num1/value)} / {int(num2/value)}'
    return result
print(Euclid(15,20))
