

# def first(stack):

#     top = stack[size]

#     return top

# def last(stack):

#     last = stack[0]

#     return last
 
# stack = [0,3,2,4,6,4,5,6,5,6,1]
 
# size = int(input("Defin the size of the stack"))

# while True:

#     action = input("Enter your action [push/pop]")

#     if len(stack) != 0:

#         if action == "pop":

#             number = int(input("Enter how many number you want to pop:"))

#             if len(stack) > size:

#                 for i in range(size-1,len(stack)):

#                     stack.pop(stack[i])

#             for j in reversed(range(len(stack)-1),len(stack)-3):

#                 stack.pop(stack[j])

#             status = input("Enter your status[y/n]")

#             if status == "N":

#                 break

#     if action == "push":

#         number = int("Enter your number: ")

#         stack.append(number)

#         if len(stack) > size:

#             for i in range(size-1,len(stack)):

#                 stack.pop(stack[i])

#         status = input("Do you want to continue (Y/N)")

#         if status == "N":

#             break

# print(stack)

class StackArray:

    def __init__(self):

        self.data = []

    def __len__(self):

        return len(self.data)

    def isempty(self):

        if len(self.data) != 0:

            return True

        return False

    def push (self , num):

        self.data.append(num)

    def pop(self ):

        if  not(self.isempty()):

            return self.data.pop()

        else:

            print("data is empty")

            return

    def top(self):

        return(self.data[len(self.data)-1])

    def last(self):

        return( self.data[0] )

stack = StackArray()

stack.push(5)

stack.push(1)

print(stack.data)

print(stack.pop())

print(stack.isempty())

print(stack.pop())

print(stack.isempty())

print(stack.push(5))

print(stack.push(6))

print(stack.top())
 
 
stack = []
 
 
while True:

    action = input("Enter your action [push/pop]")

    if len(stack) != 0:

        if action == "pop":

            stack.pop()

            status = input("Enter your status[y/n]")

            if status == "N":

                break

    if action == "push":

        number = int(input("Enter your number: "))

        stack.append(number)

        status = input("Do you want to continue (Y/N)")

        if status == "N":

            break

print(stack)

 