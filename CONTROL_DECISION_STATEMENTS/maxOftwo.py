a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
if(a>b):
    print(f"A={a} is larger ")
else:
    print(f"B={b} is larger ")
print("-----EVEN OR ODD-----")
if(a%2==0):
    print(f"A={a} is even")
else:
    print(f"A={a} is odd")
if(b%2==0):
    print(f"B={b} is even" )
else:
    print(f"B={b} is odd")