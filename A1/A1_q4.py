ref_year = "01/01/2001"
ref_day = int(ref_year[0:2])
ref_month = int(ref_year[3:5])
ref_year = int(ref_year[6:10])

dob = input("Enter dob (in dd/mm/yyyy format): ")

day = int(dob[0:2])
month = int(dob[3:5])
year = int(dob[6:10])

year_diff = abs(year - ref_year)
month_diff = abs(month - ref_month)
day_diff = abs(day - ref_day)

leap_days = int(year_diff/4)

days = year_diff * 365 + month_diff * 30 + day_diff + leap_days

if(month>ref_month):
    if(month == 2):
        days += 1
    if(month == 3):
        days += -1
    if(month == 7):
        days +=1
    if(month == 8):
        days +=2
    if(month == 10):
        days +=3
    if(month == 12):
        days +=4



print(days)

if(days < 0):
    days = -1 * days

days = days%7

if(days==0):
    print("Monday")
if(days==1):
    print("Tuesday")
if(days==2):
    print("Wednesday")
if(days==3):
    print("Thursday")
if(days==4):
    print("Friday")
if(days==5):
    print("Saturday")
if(days==6):
    print("Sunday")
