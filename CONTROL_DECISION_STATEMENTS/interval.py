#to print the interval of a given number 
num=int(input("Enter the number (0-30) : "))
if(num>=0 and num<10):
    print("It is in the range of 0-10")
elif(num>=10 and num<20):
    print("It is in the range of 10-20")
elif(num>=20 and num<30):
    print("It is in the range of 20-30")
else:
    print("Given number is <0 or >30")