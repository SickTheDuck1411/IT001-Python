class Node :
    def __init__ (self, data): 
        self.data= data
        self.link= None 
class Linkedlist:  
    def __init__ (self) :
        self.headNode =None    
    def add_end(self,data):
        n2= Node(data)
        if (self.headNode== None) : 
            self.headNode = n2
        else:
            n = self.headNode
            while n.link != None:
                n = n.link
            n.link = n2
            # self.headNode.link = n2
    def print(self):
        if self.headNode is None:
            print("Empty")
        else:
            n = self.headNode
            while n != None:
                print(n.data)
                n = n.link
    def count_ll(self):
        count =0
        n = self.headNode
        while  n != None:
            count+=1 
            n = n.link
        print(count)
    def  add_begin(self,data):
        n2=Node(data)
        n2.link = self.headNode
        self.headNode =n2 
    def delete_end(self): 
        if self.headNode == None:
            print("Empty")
        else:
            # n2=  self.headNode
            #  n1 = self.headNode.link
            n= self.headNode
            while n.link.link != None:
            #    n2 =n1 
            #    n1 = n1.link
                n= n.link
            # n2.link= None
            n.link=None
            # print(n2.data)
            # print(n1.data)
    def delete_beginning(self):
        if self.headNode == None:
            print("Empty")
        else:
            self.headNode = self.headNode.link
    def insert_after_index(self,data,range):
        new_node = Node(data)
        n = self.headNode
        index = 0
        while n.link != None :
            n = n.link
            if index == range-2:
                new_node.link = n.link  
                n.link  =  new_node
                # print(n.data)
            # print(n.data)
            index+=1
    def insert_before_index(self, data, index):

        new_node = Node(data)
        n = self.headNode
        count = 0
        if index < 0:
            return False
        elif index == 0:
            self.add_begin(data)
        else:
            while n.link != None:
                if count == index-1:
                    new_node.link = n.link
                    n.link = new_node
                    break
                else: 
                    n = n.link
                    count+=1
            if n.link == None and count<index: print("out of range")
        # if index < 0:
        #     return False
        # elif index == 0:
        #     self.add_begin(data)
        # else:
        # while n.link != None:
        #     n = n.link
        #     count+=1
        #     # if n.link == None:
        #         # return False
        #     if count == index:
        #         newNode.link = n.link
        #         n.link = newNode
    # new_node = Node(data)
        # if index <0 : 
        # count = 0
        # n = self.headNode
        # while n .link != None:
        #     n = n.link
        #     if count == index-1:
        #         new_node.link = n.link
        #         self.headNode.link = new_node   
        #     count+=1

        #phase 1: tim node phu hop
        # new_node = Node(data)
        # n = self.headNode
        # count = 0
        # # tim node truoc no,vaf concern exception

        #phase 2: thay doo
        #newNode.link= currentNode.link 
        # currentNode.link = newNode 
        #     print("Index must be positive")
        #     return False
        # if n is None or index == 0 : self.add_begin(data)
        # for  _ in  range(0, index):
        #     if n is not None: 
        #         n= n.link
        #     else : 
        #         print("out of range")
        #         return False
        # # phase 2: 
        #     newNode.link= n.link
        #     n.link= newNode


        


    def delete_at_index(self, index):
        n = self.headNode
        count = 0
        if index == 0:
            self.delete_beginning()
        elif index <0 :
            print("error")
        else:
            while n.link != None:
                if count == index-1:
                    n.link = n.link.link
                    break
                n = n.link
                count+=1
            if n.link == None and count < index: print ("out of range")             
    def linearSearch(self, key):
        n = self.headNode
        position = 0
        while n != None:
            position+=1
            if n.data == key:
                print(position)
                break
            elif n.link is None:
                print("Not found")
            else:
                n = n.link
        # return True
    def insertSort(self):
         
        return True    
        

ll = Linkedlist()
ll.add_begin(20)
ll.add_end(10)
# ll.insert_before_index(30,10)
ll.add_end(5)
ll.add_end(5)
ll.add_end(5)
ll.linearSearch(20)
# ll.delete_at_index(4)
# ll.print()
# ll.insert_after_index(7,2)
# ll.print()

# print(ll.headNode.link.link.data)
# ll.count_ll()
