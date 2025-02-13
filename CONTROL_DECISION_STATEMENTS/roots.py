#to find the roots of the quadratic equation 
a=float(input("Enter the coordinate of the x^2 : "))
b=float(input("Enter the coordinate of the x : "))
c=float(input("Enter the constant term : "))
det=b**2-4*a*c
if(det==0):
    root=-b/(2*a)
    print(f"The roots of the given equation are equal : {root}")
elif(det>0):
    root1=-b+det**0.5
    root2=-b-det**0.5
    print(f"The roots of the given equation are real and distinct roots : {root1} and {root2}")
else:
    print("The roots of the given equations are imaginary.")
    
