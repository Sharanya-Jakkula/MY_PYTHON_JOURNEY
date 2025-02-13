#to calculate factorial of a number 
num=int(input("Enter the number to find the factorial  : "))
fact=1
if(num==0):
    print(f"The factorial of the given number is {fact}")
else:
    while(num!=1):
        fact=fact*num
        num=num-1
    print(f"The factorial of the given number is {fact}")
    
