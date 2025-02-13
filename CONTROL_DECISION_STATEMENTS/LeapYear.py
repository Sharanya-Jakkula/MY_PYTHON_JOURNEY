#to check whether the given year is leap year or not 
year=int(input("Enter the year : "))
#condition-->(year%4==0 and year%100!=0)or(year%400==0)
if((year%4==0 and year%100==0)or(year%100==0 and year%400==0)):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")