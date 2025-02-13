#to calculate the area of the triangle using herons formula 
a=float(input("Enter the  length of the first side : "))
b=float(input("Enter the  length of the second side : "))
c=float(input("Enter the  length of the third side : "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is {}".format(area))