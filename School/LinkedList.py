class Node: 
    
    def __init__(self,data): 
        self.data=data 
        self.link=None #initialize

class LinkedList: 
    
    def __init__(self): 
        self.head=None #Create an empty linked list
    
    def print_LL(self): 
        if self.head is None:   
            print("Linked List is empty") 
        else: 
            n=self.head #a variable to represent the head 
            while n is not None: 
                print(n.data,"--->",end=" ") 
                n=n.link 
    
    def add_begin(self,data): 
        new_node=Node(data) #Create New Node 
        new_node.link=self.head #Change the link from the old node
        self.head=new_node
    
    def add_end(self,data): 
        new_node=Node(data)
        if self.head is None: 
            self.head = new_node 
        else: 
            n=self.head 
            while n.link is not None: 
                n=n.link 
            n.link=new_node
    
    def delete_beginning(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            self.head=self.head.link
    
    def delete_end(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n.link.link is not None:
                n = n.link
            n.link = None
    
    def count_list(self):
        n = self.head
        count = 0
        while n is not None:
            count+=1        
            n = n.link
            print(count)
 
LL1=LinkedList() 
LL1.add_begin(10) 
LL1.add_begin(20) 
LL1.add_begin(30) 
LL1.add_end(5)
LL1.add_end(1)
LL1.print_LL()
LL1.delete_beginning()
print()
LL1.print_LL()
LL1.count_list()