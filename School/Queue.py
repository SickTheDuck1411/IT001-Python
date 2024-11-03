# arr = [9,8,9,3,2,1,4,3]

# while True:

#     action = input("Enter your action[E/D]")

#     if action == "E":

#         number = int(input("Enter your number:"))

#         arr.append(number)

#         status = input("Do you want to continue(Y/N)")

#         if status == "N":

#             break

#     if action == "D":

#         if len(arr) !=0 :

#             arr.pop(0)

#         else:

#             print("array is empty")

#         status = input("Do you want to continue(Y/N)")

#         if status == "N":

#             break
 
 
 
class Classqueue():

    def __init__(self):

        self.data = []

    def enqueue(self,num):

        return self.data.append(num)

    def dequeue(self):

        if len(self.data)!=0:

            return self.data.pop(0)

        return False

    def first(self):

        return(self.data[0])

A = Classqueue()

A.enqueue ( 8 )

A.enqueue ( 9 )

print( A.data )

A. dequeue()

A. dequeue()

print(A)
 