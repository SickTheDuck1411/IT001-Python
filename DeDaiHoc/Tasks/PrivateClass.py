class SonGo(): 
    def __init__(self, keo):
        self.keo= keo
    def GetValue(self):
        print(self.keo)
    def CheckInventory(self):
        return self.__CalculateFormula()  
    def __CalculateFormula(self):
        return self.keo*100/70
    