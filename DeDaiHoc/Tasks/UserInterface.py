import pandas as pd
from CustomDate import CustomDate 
# def

# # Main

testDate  = CustomDate('10/10/2024','dd/mm/yyyy')
print(testDate.AddMonths(3))





# data = pd.read_csv('./hsd.csv', delimiter=';')
# tgsd = data['TGSD']
# nsx = data['NSX']



# information = Custom(month,year)
# remainder = information.findremainder(tgsd)
# interger = information.findinterger(tgsd)

# for i in range(0,25):
#     LimitYear = year+remainder[i]
#     LimitMonth = month+interger[i]

# # for i in range(0,len(data)):
# #     LimitYear= (year+tgsd[i])%2
# #     LimitMonth = (month+tgsd[i])/2
# #     # print(LimitMonth,LimitYear)
