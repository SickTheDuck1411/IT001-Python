class Node():
    def __init__(self,data):
        self.data = data
        self.link = None

class DisplayLinkedList():
    def display(self):
        n = self.headnode
        while n.link !=None:
            print(n.data,"-->", end=" ")
            n=n.link
        print(n.data, end=" ")
         
    
class Queue(DisplayLinkedList) :
    # def __init__(self):
    #     self.headnode = None
    # def addbegining(self,data):
    #     newnode = Node(data)
    #     newnode.link = self.headnode
    #     self.headnode = newnode
    # def addend (self,data):
    #     newnode = Node(data)
    #     if self.headnode == None:
    #         self.headnode = 
    def __init__(self):
        self.headnode = None
    def enqueue(self,data):
        newnode = Node(data)
        if self.headnode == None:
            self.headnode = newnode
        else:
            n = self.headnode
            while n.link != None:
                n = n.link
            n.link = newnode
    def dequeue(self):
        if self.headnode == None:
            print("empty")
        else:
            self.headnode = self.headnode.link
        #code tuyen
        # while n != None:
        #      print(n.data ,  end="")
        #      if n.link != None:
    #             print("-->" , end="")
    #             n = n.link
        #code thien
        # while n.link != None: 
        #     print(n.data,"-->" , end="")
        #     n= n.link
        # print(n.data , end="")
        
        #     # else:
                # ak
        # if self.headnode == None:
        #     print("Empty")
        # elif n != 0 :
class Stack (DisplayLinkedList):
    def __init__(self):
        self.topnode = None
    def push(self,data):
        newnode = Node(data)
        newnode.link = self.topnode
        self.topnode = newnode
    def pop(self):
        if self.topnode == None:
            print("empty")
        else:
            self.topnode = self.topnode.link
# a = Stack()   
# a.push(20)
# a.push(40)        
# a.push(60)        
# a.push(80)



# a.dispplay()


a = Queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.enqueue(40)
a.dequeue()
a.display()
        