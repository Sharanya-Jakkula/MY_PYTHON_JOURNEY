P=float(input("Enter the principle amount : "))
T=float(input("Enter the Time period : "))
R=int(input("Enter the rate of interest : "))
SI=(P*T*R)/100
print("SIMPLE INTEREST : ",SI)
CI=P*((1+(R/100))**T)
print("COMPOUND INTEREST : ",CI)