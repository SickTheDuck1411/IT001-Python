class node():
    def __init__(self,data):
        self.next = None
        self.data = data
class CLL():
    def __init__(self):
        self.head = None
        self.tail = None
    def display(self):
        if self.head is None:
            print("The linked list is empty:")
        else:
            temp = self.head
            print(temp.data , "-->" , end="")
            while(temp.next != self.head):
                temp = temp.next
                print(temp.data,"-->" , end="")
            print(self.head.data)
    def add_begin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

l = CLL()
n1 = node(10)
l.head = n1
l.tail = n1
n2 = node(20)
l.tail.next = n2
l.tail=n2
n3 = node(30)
l.tail.next = n3
l.tail=n3
l.tail.next = l.head
l.display()