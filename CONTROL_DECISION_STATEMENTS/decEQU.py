#to find the decimal equivalent of given binary number
n=int(input("Enter the binary number to find its decimal number : "))
l=len(str(n))
i=0
r=0
dec=0
while(i<l):
    r=n%10
    dec=dec+r*pow(2,i)
    i+=1
    n=n//10
print(f"The decimal equivalent of given number is {dec}")
    

