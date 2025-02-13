#to create a tic tac toe game
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
#a=input("Enter the symbol : ")
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
#display(row1,row2,row3)
row1[1]='X'
display(row1,row2,row3)
i=0
p1=0
row=0
sym=' '
while(i<8):
    row=int(input("Enter the row number (1,2,3): "))
    pos=int(input("Enter the position : "))
    sym=input('Enter the symbol : ')
    if(row==1):
        if(row1[pos]==' '):
            row1[pos]=sym
            display(row1,row2,row3)
    elif(row==2):
        if(row2[pos]==' '):
            row2[pos]=sym
            display(row1,row2,row3)
    elif(row==3):
        if(row3[pos]==' '):
            row3[pos]=sym
            display(row1,row2,row3)
    else:
        print("Invalid row")
    i+=1
    