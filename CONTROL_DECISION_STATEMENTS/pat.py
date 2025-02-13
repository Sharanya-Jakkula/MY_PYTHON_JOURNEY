#to print the pattern
n=int(input("Enter the size of the pattern  : "))
p=n
c=1
for i in range(n):
    c=i+1
    for h in range(i+1):
        print(" ",end="")
    for k in range(p):
        print(c,end=" ")
        c+=1
    p-=1
    print()
'''
1 2 3 4 5 
  2 3 4 5 
   3 4 5 
    4 5 
     5 
'''