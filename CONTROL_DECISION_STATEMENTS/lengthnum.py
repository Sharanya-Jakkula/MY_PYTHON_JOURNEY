#to determine the length of the given number 
num=int(input("Enter the number : "))
len=0
if(num==0):
    print("The length of the number : 1")
else:
    while(num!=0):
        len+=1
        num=num//10
    print(f"The length of the number : {len}")