#to print the calender of the given year
import calendar
y=int(input("Enter the year : "))
m=1
print("\n********CALENDER**********\n")
cal=calendar.TextCalendar(calendar.SUNDAY)
i=1
while i<=12:
    cal.prmonth(y,i)
    i+=1
#calender instance 
