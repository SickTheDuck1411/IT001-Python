from DateUtil import CheckValid,SplitDate,MaximumDay,ConvertDateComponent
class CustomDate():
    def __init__(self,date,formatDate = 'dd/mm/yyyy'):
        self.date = date
        self.formatDate = formatDate
        if CheckValid(date, formatDate): 
            day,month, year = SplitDate(date,formatDate)
            self.day=day
            self.month= month
            self.year= year
            self.valid= True

        else:
            print('You need to change the suitable date') 
            self.valid = False
    def AddMonths(self, value):
        if not self.valid: 
            print('You need to change')
            return False

        addedMonth = self.month + value
        if addedMonth > 12:
            self.year = self.year + int(addedMonth/12)
            self.month = addedMonth % 12 
        else:
           
           self.month = addedMonth
        if self.day > MaximumDay(self.month,self.year):
            self.day = self.day % MaximumDay(self.month,self.year)
            self.month = self.month + 1
        return self.GetDate()

    def GetDate(self):
        formatedDay = ConvertDateComponent(self.day)    
        formatedMonth = ConvertDateComponent(self.month)       
        date= self.formatDate.replace('dd',formatedDay).replace('mm',formatedMonth).replace('yyyy',str(self.year))
        return date
        
    def SubstractMonths(self,value):
        print('Substract MOnths')
    
# print(CheckValid('11/12/2004'))
# print(CheckValid('11/12/2004', 'dd/mm/yyyy'))
# print(CheckValid('11/12/2004', 'mm/dd/yyyy'))
# print(CheckValid('11-12-2004', 'dd-mm-yyyy'))
# print(CheckValid('11-12-2004', 'mm-dd-yyyy'))
# #error
# print(CheckValid('11/12/2004', 'mm-dd-yyyy'))

# print(CheckValid('15/12/2004', 'mm/dd/yyyy'))

