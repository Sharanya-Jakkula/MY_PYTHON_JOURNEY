#getpass module
import getpass
password=getpass.getpass(prompt="Enter the password  : ")
if password=='oxford':
    print("Welcome")
else:
    print("Incorrect password")