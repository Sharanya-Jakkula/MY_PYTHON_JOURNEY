#to check whether the given character is  lower or upper and returning its converse case
char=input("Enter the character : ")
if(char<='Z' and char>='A'):
    print(f"The entered character is is in upper case and its lower case is {char.lower()}")
elif(char>='a' and char<='z'):
     print(f"The entered character is is in lower case and its upper case is {char.upper()}")
else:
    print("Please enter a character !!")