def SplitDate(date, formatDate):
    formatDate = str(formatDate).lower()
    
    if formatDate[2] != date[2]: return False
    
    match(formatDate):
        case 'dd/mm/yyyy': 
            dateComponent = date.split('/')
            day = dateComponent[0]
            month = dateComponent[1]
            year = dateComponent[2]
        case 'mm/dd/yyyy': 
            dateComponent = date.split('/')
            day = dateComponent[1]
            month = dateComponent[0]
            year = dateComponent[2]
        case 'dd-mm-yyyy':
            dateComponent = date.split('-')
            day = dateComponent[0]
            month = dateComponent[1]
            year = dateComponent[2]
        case 'mm-dd-yyyy':
            dateComponent = date.split('-')
            day = dateComponent[1]
            month = dateComponent[0]
            year = dateComponent[2]
        case _ :
            return False
    return int(day),int(month),int(year)     

def CheckLeapYear(year):
    if  year%4 == 0 and year % 100 != 0:
       return True
    else:   return False    

def MaximumDay(month,year):
    MaximumDay = 0
    thirtyOneDays  = [1,3,5,7,8,10,12] 
    thirtyDays = [4,6,9,11]
    if month in thirtyDays:
        MaximumDay = 30
    if month in thirtyOneDays:
        MaximumDay = 31
    else:
        if CheckLeapYear(year) :
            MaximumDay = 29
        else:
            MaximumDay= 28
    return MaximumDay

def CheckValid(date,formatDate): 
    if len(date) != len(formatDate): return False
    resultedDate = SplitDate(date,formatDate)
    if not resultedDate: return False
    day = (resultedDate[0])
    month = (resultedDate[1])
    year = (resultedDate[2])
    
    if month <1 or month > 12 : return False 
    
    if day<= MaximumDay(month,year):
       return True
    else:
        return False 

def ConvertDateComponent(value): 
    formatedValue = ''  
    if value > 9:
        formatedValue = str(value)
    else:
        formatedValue = '0'+ str(value)
    return formatedValue