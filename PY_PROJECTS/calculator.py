#to program a calculator
choice=0
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def exp(a,b):
    return a**b
print("1-addition\n2-subtraction\n3-multiplication\n4-division\n5-modulus\n6-exponent\n7-exit")
choice=int(input("Enter your choice : "))
while(True):
    if(choice==7):
        print("Thank You for using the calculator\nBye..")
        break
    a=int(input("Enter first operand : "))
    b=int(input("Enter the second operand : "))
    print("------------------------------------------")
    if(choice==1):
        print(f"Addition of two numbers is {add(a,b)}")
    elif(choice==2):
        print(f"Subtraction of two numbers is {sub(a,b)}")
    elif(choice==3):
        print(f"Multiplication of two numbers is {mul(a,b)}")
    elif(choice==4):
        if(b==0):
            print("not possible")
        else:
            print(f"Division of two numbers is {div(a,b)}")
    elif(choice==5):
        if(b==0):
            print("not possible")
        else:
            print(f"Modulus of two numbers is {mod(a,b)}")
    elif(choice==6):
        print(f"Power of two numbers is {exp(a,b)}")
    else:
        print("Please enter as per the instructions ")
    print("------------------------------------------")
    print("1-addition\n2-suntraction\n3-multiplication\n4-division\n5-modulus\n6-exponent\n7-exit")
    choice=int(input("Enter your choice : "))