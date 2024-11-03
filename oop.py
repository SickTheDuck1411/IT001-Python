# #x1 -> x5
# #y1 -> y5
# def dientich(x,y):
#     return x*y

class Rectangle:
    def __init__(self,width,length):
        self.width= width
        self.length= length
    def calculateArea(self):
        return self.width*self.length
    def calculatePerimeter(self):
        return (self.width+self.length)*2


class Square:
    def __init__(self,side):
        self.side = side
    def calculateArea(self):
        return self.side*self.side
    def calculatePerimeter(self):
        return (self.side)*4
    

# công nhan name age, lamtai, address
# name  age, hoctai, address
#name  age, day tai, address


#congnguowi : name, age, address
#giao vien: connguoi, lam tai 
# hocsinh : connguoi, hoc tai
# congnhan: connguwoi, lam tai



r1 = Rectangle(2,3)
print(r1.calculatePerimeter())
r3 = Rectangle(2,3)
print(r1.calculatePerimeter())
r2 = Rectangle(2,3)
print(r1.calculatePerimeter())

s1= Square(4)
print(s1.calculatePerimeter())

