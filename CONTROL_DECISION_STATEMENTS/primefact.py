# to find the prime factors of the given number 
num=int(input("Enter the number to find the prime factors : "))
i=1
c=0
if(num==0 or num==1):
    print("No prime factors")
else:
    for i in range(1,num+1):
        if(num%i==0):
            c=0
            for j in range(1,i+1):
                if(i%j==0):
                    c+=1
            if(c==2):
                print(i)