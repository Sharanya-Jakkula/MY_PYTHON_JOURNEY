from datetime import date
date_components = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
print(date_components)
year, month, day = [int(item) for item in date_components]
d = date(year, month, day)
print(d)

'''d1=int(input("Enter the joining date : "))
m1=int(input("Enter the joining month : "))
y1=int(input("Enter the joining year : "))
d2=int(input("Enter the relieving date : "))
m2=int(input("Enter the relieving month : "))
y2=int(input("Enter the relieving year : "))
start=date(y1,m1,d1)
end=date(y2,m2,d2)
print("------------------------------------------")
print(f"The joining date of the employee is {start}")
print(f"The relieving date of the employee is {end}")
print(f"The number of days employee worked is {(end-start).days} days")'''
#can perform any operations on the date 


