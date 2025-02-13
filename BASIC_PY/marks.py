#calculate percent
e1=int(input("Enter marks of first subject : "))
e2=int(input("Enter marks of second subject : "))
s1=int(input("Enter score in sports : "))
a1=int(input("Enter the score in activity1 : "))
a2=int(input("Enter the score in activity2 : "))
a3=int(input("Enter the score in activity3 : "))
e=(e1+e2)*50/200
s=(s1*20)/50
a=((a1+a2+a3)*30)/60
print("EXAM PERCENTAGE : ",e)
print("SPORTS PERCENTAGE : ",s)
print("ACTIVITIES PERCENTAGE : ",a)
print("Total percentage obtained : ",(e+s+a))


