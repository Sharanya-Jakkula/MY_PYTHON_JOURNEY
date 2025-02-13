#to find whether the given number is a power of two
x=int(input("Enter the number to find whether the given number is a power of two : "))
if(x!=0 and (x&(x-1))==0):
    print("The given number is a power of two")
else:
    print("The given number is not a power of two")

