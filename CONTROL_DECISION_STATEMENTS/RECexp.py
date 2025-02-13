#to find the exponent using recursion
def exp(a,b):
    if(b==0):
        return 1
    else:
        return a*exp(a,b-1)
a=int(input("Enter the base : "))
b=int(input("Enter the exponent : "))
print(exp(a,b))