#to find the binary equivalent of the given decimal
import math
#binary conversion
def binary(num):
    res=0
    rem=0
    i=0
    while(num!=0):
        rem=num%2
        res=res+rem*pow(10,i)
        num=num//2
        i+=1
    print(f"The binary equivalent of the given number {num} is {res}")
#octal conversion
def octal(num):
    res=0
    rem=0
    i=0
    while(num!=0):
        rem=num%8
        res=res+rem*pow(10,i)
        num=num//8
        i+=1
    print(f"The octal equivalent of the given number {num} is {res}")
#hexadecimal conversion
def hexa(num):
    res=0
    rem=0
    i=0
    while(num!=0):
        rem=num%16
        res=res+rem*pow(10,i)
        num=num//16
        i+=1
    print(f"The hexadecimal equivalent of the given number {num} is {res}")
num=int(input("Enter the decimal number to find its binary equivalent : "))
binary(num)
octal(num)
hexa(num)

    
