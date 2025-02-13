#to print the different pattern
n=int(input("Enter the size of the pattern : "))
c=0
for i in range(n):
    c=i+1
    for j in range(i+1):
        print(c,end=" ")
        c-=1
    for k in range(1,i+1):
        print(k+1,end=" ")
    print()