#to print the floyd's traingle
n=int(input("Enter the number of rows to print the floyd's triangle : "))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end="  ")
        p+=1
    print() 