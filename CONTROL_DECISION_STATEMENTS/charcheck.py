#to check the given character
char=input("Enter the character : ")
if char.isalpha():
    print("It is a character")
elif char.isdigit():
    print("It is a digit")
elif char.isspace():
    print("It is a white space ")
else:
    print("It is something special")