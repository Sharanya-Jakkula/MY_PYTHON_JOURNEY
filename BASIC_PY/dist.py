x1=int(input("Enter the x1 : "))
y1=int(input("Enter the y1 : "))
x2=int(input("Enter the x2 : "))
y2=int(input("Enter the y2 : "))
x=(x1-x2)**2
y=(y1-y2)**2
dist=(x+y)**0.5
print("The distance between ({},{}) and ({},{}) is {}".format(x1,y1,x2,y2,dist))