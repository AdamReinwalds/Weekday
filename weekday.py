VECKO_DAG = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
MONTH_LIST_31 = [1, 3, 5, 7, 8, 10, 12]
MONTH_LIST_30 = [4, 6, 9, 11]

while True:
    year = input("Year: ")
    if year.isdigit():
        year = int(year)
        if year < 1583 or year >9999:
            print("Out of allowed range 1583 to 9999")
        else:  
            break
    else:
        print("Only numbers allowed")

while True:
    month = input("Month: ")  
    if month.isdigit():
        month = int(month)
        if month < 1 or month > 12:
            print("Out of allowed range 1 to 12")     
        else:
            break 
    else: 
        print("Only numbers allowed")  

if month in MONTH_LIST_31:
    dayAmount = 31
elif month in MONTH_LIST_30:
    dayAmount = 30
else:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        dayAmount = 29
    else:
        dayAmount = 28

while True:
    day = input("Day: ")
    if not day.isdigit():
        print("Only numbers allowed")
    else:
        day = int(day)
        if day > dayAmount:
            print("Out of allowed range 1 to", dayAmount)
        else:
            break

if month == 1 or month == 2:
 month += 12
 year -= 1 

weekday = ((day + 13 * (month + 1) // 5 + year + year // 4
 - year // 100 + year // 400) % 7)

print("It is a", VECKO_DAG[weekday])