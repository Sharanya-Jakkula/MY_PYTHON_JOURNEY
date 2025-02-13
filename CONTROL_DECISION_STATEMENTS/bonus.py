#a company decides to give bonus to the employee based on the  salary and the gender
sal=float(input("Enter the salary : "))
g=input("Enter the gender ('m' or 'f') : ")
bonus=0
m=0.05
f=0.10
if(sal<10000):
    if(g=='m'):
        bonus=sal*(m+0.02)
    else:
        bonus=sal*(f+0.02)
    print(f"Total amount to be paid is {bonus+sal}")
else:
    if(g=='m'):
        bonus=sal*(m)
    else:
        bonus=sal*(f)
    print(f"Total amount to be paid is {bonus+sal}")
    