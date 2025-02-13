num=0
pos=0
neg=0
sumpos=0
sumneg=0
while(1):
    num=int(input("Enter : "))
    if(num<0):
        pos=pos+1
        sumpos+=num
    else:
        neg+=1
        sumneg+=num
    if(num==-1):
        break
print(f"Count of positive numbers : {pos}")
print(f"Sum of the positive numbers : {sumpos}")
print(f"Count of negative numbers : {neg}")
print(f"Sum of the negative numbers : {sumneg}")
print(f"Average of positive numbers : {sumpos/pos}")
print(f"Average of negative numbers : {sumneg/neg}")

    