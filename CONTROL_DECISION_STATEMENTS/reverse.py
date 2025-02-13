#to find the reverse of the given number
import math 
num=int(input("Enter the number : "))
rem=0
rev=0
len=0
temp=num
while(num!=0):
    num=num//10
    len+=1
print(len)
num=temp
sum=0
i=0
while(len!=0):
    rem=num%10
    sum=sum+rem
    rev=rev+rem*pow(10,len-1)
    len-=1
    num=num//10
print(f"The sum of the digits of the given number is {sum}")
print(f"The reverse of the number is : {rev}")