#to check whether the number is palindrome or not
num=int(input("Enter number : "))
length=len(str(num))
rem=0
rev=0
temp=num
i=0
while(length!=0):
    rem=num%10
    rev=rev+rem*pow(10,length-1)
    length-=1
    num=num//10
#print(f"The reverse of the number is : {rev}")
if(rev==temp):
    print("The given number is a palindrome ")
else:
    print("The given number is not a palindrome")