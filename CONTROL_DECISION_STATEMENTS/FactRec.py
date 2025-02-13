#to print the factorial using the recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the value of n : "))
print(fact(n))