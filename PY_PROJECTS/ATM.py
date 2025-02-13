#to demonstrate the ATM Management
global amount
def deposit(amt):
    global amount
    amount+=amt
    print(f'{amt} is deposited into your account')
    return amount
def withdraw(amt):
    global amount
    if(amount>=amt):
        amount-=amt
        print(f'{amt} is withdrawn from your account')
    else:
        print('Insufficient balance')
def ministatement():
    print('--------------------ATM---------------------------')
    print(f'Name : kiran\nAge : 40\nBalance : {amount}\nThank you!!!')
    print('--------------------------------------------------')

username='kiran'
password='python123'
c_name=input('Enter your username : ')
c_password=(input('Enter your password : '))
if (c_name==username and c_password==password):
    amount=50000
    print('''
          1.Deposit
          2.Withdraw
          3.Ministatement
          4.Exit
          ''')
    option=int(input('Select your option : '))
    while(True):
        if(option==1):
            amt=int(input("Enter the amount to be deposited : "))
            deposit(amt)
        elif (option==2):
            amt=int(input("Enter the amount to be withdrawn : "))
            withdraw(amt)
        elif(option==3):
            ministatement()
        elif(option==4):
            print("Thank you!!!!")
            break
        else:
            print("Enter the option correctly")
        print('''
          1.Deposit
          2.Withdraw
          3.Ministatement
          4.Exit
          ''')
        option=int(input("Select your option : "))
    








