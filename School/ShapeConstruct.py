def PrintRectangle(value,numOfRow,numOfColumn):
    array =[]
    for i in range(0, numOfRow):
        if i== 0 or i == numOfRow -1:
            subarray=[]
            for j in range(0,numOfColumn):
              subarray.append(value)
            array.append(subarray)
        else:
            subarray=[value, value]
            for i in range(0,numOfColumn-2):
                subarray.insert(1,0)
            array.append(subarray)  
    return array

def PrintTriangle(value, row):
    for i in range(0,row):
        result = ''
        if i== 0:
            for _ in range(0,row-1):
                result= result+ ' '
            result = f'{result}{value}'
        elif i == row -1: 
            result= ''
            for _ in range(0, row):
                result+= f'{value} '
        else:
            result =''
            for _ in range(0,row - i-1):
                result += ' '
            result+=f'{value}'
            for _   in range(0,2*i-1):
                result += ' '
            result+=f'{value}'
        print(result)

# PrintRectangle(9,4,6)
# PrintTriangle(9,6)

# row = 10
# column = 6
# number = int(input("Enter your number:"))
# array = []
# rectangleArray= PrintRectangle(number, 4, 6)
# Def
def Rectangle(row,column,value):
        
    for i in range(0,row):
        if i == 0 or i == row-1:
            for j in range(0,column):
                print(value,end=" ")
            print()
        elif i>0 or i<row-1:
            for j in range(0, column):
                if j == 0 :
                    print(value,end=" ")
                elif  j== column-1:
                    print(value)

                else:
                    print(' ',end=" ")
def Triangle(row,number):
    column = row
    # outerspace = column-1
    # centrespace = 2
    for i in range(0,row):
        if i == 0 :
            # for j in reversed(range(0,column-1)):
            #     if j != 0:
            #         print('',end=" ")
            #     else:
            #         print('',number)
            
            # add space for correct position
            for _ in range(0, column-2):
                print('',end=" ")
            # print value at correct position            
            print('',number)

        elif i == row-1:
            for _ in range(0,column):
                print(number,end=" ")
        else:
            
            # for j in range(0,outerspace):
            #     if j == outerspace-1:
            #         print(number,end="")
            #     else:
            #         print(' ',end="")
            # outerspace-=1
            for _ in range(0, column-i-1):    
                print(' ',end="")
            print(number,end="")
            
            # for j in range(0,centrespace):
            #     if j == centrespace-1:
            #         print(number)
            #     else:
            #         print(' ',end="")
            # centrespace+=2
            
            
            for _ in range(0,(2*i)-1):
                print(' ',end="")
            print(number)


# Main
# number = int(input("Enter your number: "))
# row = int(input("Enter your row: "))
# column =int(input("Enter your column: "))
rectangle = Rectangle(4,6,9)
triangle = Triangle(6,9)


# Rectangle
# for i in range(0,4):
#     if i == 0 or i == 3:
#         for j in range(0,column):
#             print(number,end=" ")
#         print()
#     elif i==1 or i==2:
#         for j in range(0, column):
#             if j == 0 :
#                 print(number,end=" ")
#             elif  j== column-1:
#                 print(number)

#             else:
#                 print(' ',end=" ")

# Triangle
# centrespace = 2
# outerspace = 5
# for i in range(0,6):
#     if i == 0 :
#         for j in reversed(range(0,column-1)):
#             if j != 0:
#                 print('',end=" ")
#             else:
#                 print('',number)
#     elif i == 5:
#         for _ in range(0,column):
#             print(number,end=" ")
#     else:
#         for j in range(0,outerspace):
#             if j == outerspace-1:
#                 print(number,end="")
#             else:
#                 print(' ',end="")
#         outerspace-=1
#         for j in range(0,centrespace):
#             if j == centrespace-1:
#                 print(number)
#             else:
#                 print(' ',end="")
#         centrespace+=2


    
# print('     9')
# print('    9 9')
# print('   9   9')
# print('  9     9')
# print(' 9       9')
# print('9 9 9 9 9 9')

# print(array)
# print(rectangleArray)










# for i in range(0,row):
#     if i==0 or i==3 or i == row-1:
#         print(number,number,number,number,number,number,number, sep=' ')       
#     elif i < 3:
#         print(number,' ',' ',' ',' ',' ',number, sep=' ')
#     else:

#         print('wait')       
#     # for j in range(0, column):
#     #     if i == 0 or i == 3 :
#     #         array1.append(number)
#     #     elif  i < 3:
#     #         if j == 0 or j == column-1:
#     #             array1.append(number)
#     #         array1.append("0")  
#     # array.append(array1)
# for i in range(0,6):
#     for j in range(0,10):
# array = [3,3,3,3,3,3,3,3]
#     for i in array:
#         print(i,end=' ')

# # print(*array,sep=" ")

# # print(9,9,9,9,9,9,9,9,9,sep=" ")

# # print(9,sep="\n")

# array =[]
# for i in range(0,3):
#     subarray =[1,2,3,4]
#     array.append(subarray)
# print(array)










