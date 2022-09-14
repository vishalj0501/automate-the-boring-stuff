import re

def valid(date):
    if int(date[0])>31:
        return 'Invalid Date'

    elif int(date[1])>12:
        return 'Invalid Date'

    elif int(date[0])>30:
        if int(date[1]) in [2,4,6,9,11]:
            return 'Invalid Date'

    elif int(date[0])>29 and date[1]=='02':
        return 'Invalid Date'

    elif date[1]=='02':
        if int(date[2])%4==0 and (int(date[2])%100 !=0 or int(date[2])%400==0):
            if date[0]==29:
                return 'Invalid Date'

    elif date[1]=='02' and int(date[0])>28:
        return 'Invalid Date'
        
    return 'Valid Date'


date_reg= re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')

date_real=str(input("Enter Date DD/MM/YYYY format: \n"))
dates=date_reg.search(date_real)
date_list=[]

for i in range(0,3):
    date_list.append(dates.group(i+1))

print(valid(date_list))




   



