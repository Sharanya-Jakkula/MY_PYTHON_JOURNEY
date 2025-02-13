#to print the series of numbers upto given range
n=int(input("Enter the number upto which you want to print the series : "))
sum=0
for i in range(1,n+1):
    r=1/i#r=1/i**2 or r=1/i**3  or r=i/i+1
    sum=sum+r
print(f"The sum of the series is : {round(sum,2)}")
#round() is used to round off something upto given number of places