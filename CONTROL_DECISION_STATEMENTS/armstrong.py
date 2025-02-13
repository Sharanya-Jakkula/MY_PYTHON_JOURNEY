#to check whether the given number is armstrong or not
num=int(input("Enter the number : "))
l=len(str(num))
sum=0
temp=num
rem=0
while(num!=0):
    rem=num%10
    sum=sum+pow(rem,l)
    num=num//10
if(sum==temp):
    print("The given number is Armstrong number ")
else:
    print("It is not an armstrong number ")