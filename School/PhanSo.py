from PhanSoUtil import simplify
class Phanso():
    def __init__(self, numerator, denominator):
        if denominator != 0: 
        #     self.n= numerator
        #     self.d=denominator
        #     self.__simplify()21
            remainder = simplify(numerator,denominator)
            self.n= int(numerator/remainder)
            self.d=int(denominator/remainder)
        
        else: 
            print('Phan so nay khong ton tai')
            return False
        
    
    def Display(self):
        print(f'Phan so la:{self.n} / {self.d}')
        
    def __add__(self,other):
        #tinh toan
        numerator1 = self.n
        denominator1 = self.d
        numerator2 = other.n
        denominator2 = other.d  

        resltedDenominator = denominator1 * denominator2
        resultedNumerator = numerator1 * denominator2 + numerator2 * denominator1
        
        return Phanso(resultedNumerator,resltedDenominator)
    def __sub__(self,other):
        numerator1 = self.n
        denominator1 = self.d
        numerator2 = other.n
        denominator2 = other.d  

        resltedDenominator = denominator1 * denominator2
        resultedNumerator = numerator1 * denominator2 - numerator2 * denominator1
        
        return Phanso(resultedNumerator,resltedDenominator)
        
    def __mul__(self, other): 
        numerator1 = self.n
        denominator1 = self.d
        numerator2 = other.n
        denominator2 = other.d  

        resltedDenominator = denominator1 * denominator2
        resultedNumerator = numerator1 * numerator2 
        
        return Phanso(resultedNumerator,resltedDenominator)
    def __truediv__(self,other):
        numerator1 = self.n
        denominator1 = self.d
        denominator2 = other.n
        numerator2 = other.d  
        resltedDenominator = denominator1 * denominator2
        resultedNumerator = numerator1 *  numerator2 
        return Phanso(resultedNumerator,resltedDenominator)
    def __lt__(self,other):
        numerator1 = self.n
        denominator1 = self.d
        numerator2 = other.n
        denominator2 = other.d
        New1 = numerator1* denominator2
        New2 = numerator2* denominator1
    
        if(New1 < New2) :        
            return True
        else:
            return False
            
    def __gt__(self,other):
        numerator1 = self.n
        denominator1 = self.d
        numerator2 = other.n
        denominator2 = other.d
        New1 = numerator1* denominator2
        New2 = numerator2* denominator1
    
        if(New1 > New2) :        
            return True
        else:
            return False
    def __eq__(self,other):
        numerator1 = self.n
        denominator1 = self.d
        numerator2 = other.n
        denominator2 = other.d
        if numerator1!= numerator2 or denominator1!= denominator2: return False
        else: return True
            
# Nguoi cos ten 
# class GiaoVien(Nguoi):
#     bang cap 
# # giao vien laf nguwofi dayj hocj  bang cpa 
# class Nguoi():
#     ten 
#     ttuoi
# may van hieu laf cos con nguwofi 

# class GiaoVien ext
# # khi nguowfi dungf nhap vaof thif cos there phan soos dods chuaw ruts gon 
# #phair turn goj 

phanso1= Phanso(7,8)
phanso2= Phanso(8,9)
if (phanso1< phanso2):
    print('phan so 1 nho hon')
else : 
    print('phan so 1 khong nho hon')
