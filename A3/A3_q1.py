def week_day_name(index):
    if index==0: return "Sun"
    elif index==1: return "Mon"
    elif index==2: return "Tue"
    elif index==3: return "Wed"
    elif index==4: return "Thu"
    elif index==5: return "Fri"
    elif index==6: return "Sat"

def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def days_in_month(month , year=1990):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30


def date_value(day ,month, year):
    value=0
    y=year-1
    value = y * 365 + y//4  - y//100 + y//400
    m=1
    while m<month:
        value+= days_in_month(m,year)
        m+=1

    value+=day
    return value

def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return week_day_name(diff)

def day_index(day):
    if day == "Sun": return 0
    elif day == "Mon": return 1
    elif day == "Tue": return 2
    elif day == "Wed": return 3
    elif day == "Thu": return 4
    elif day == "Fri": return 5
    elif day == "Sat": return 6

def calender(month,year):
    day = date_to_week_day(1,month,year)
    days = days_in_month(month)
    index = day_index(day)
    
    month =[]
    week = []

    shift = 0 
    while shift<index:
        week.append("  ")
        shift += 1

    count = 1
    while count<= days:
        if(len(week)==7):
            month.append(week)
            week = []
            week.append(str(count).zfill(2))
        else:
            week.append(str(count).zfill(2))

        count += 1 
    month.append(week)
    #print(month)
    return month


def print_calender(month):
    for week in month:
        for day in week:
            print(day," ", end=" ")
        print()



def transpose_month(month):
    rev_month =[]
    row=[]
    day = 0
    while day <7:
        row.append(week_day_name(day))
        rev_month.append(row)
        row = []
        day += 1
        
    for i in range(len(month[0])):
        for item in month:
            rev_month[i].append(item[i])
    return rev_month
 
month = calender(9,2023)
rev_month = transpose_month(month)
print(rev_month)
print_calender(rev_month)