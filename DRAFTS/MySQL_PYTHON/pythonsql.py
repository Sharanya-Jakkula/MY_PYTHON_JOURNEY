import _mysql_connector
import getpass4
name=input("Enter the username  : ")
pwd=getpass4.getpass("Enter the password : ")
if(name=='root' and pwd=='123'):
    print("login successful")
else:
    print("Login was unsuccessful please enter the correct username and password")