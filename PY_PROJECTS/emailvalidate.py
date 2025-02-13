email=input("Enter the email address : ")
k=0
j=0
d=0
if len(email)>=6:#g@g.com
    if(email[0].isalpha()):
        if ("@" in email) and (email.count("@")==1):
            if(email[-4]=='.')^(email[-3]=='.'):#dot should be in 4 or 5 place from last 
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=='_' or i=='@' or i=='.':
                        continue
                    else:
                         d=1
                         
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                else:
                    print("Right email ")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
            