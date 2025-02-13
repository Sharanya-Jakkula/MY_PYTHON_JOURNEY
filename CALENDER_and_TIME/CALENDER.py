#to print the calender by taking the start day
month=input("Enter the name of the month : ").lower()
print("\n(0-Sun\t1-Mon\t2-Tue\t3-Wed\t4-Thu\t5-Fri\t6-Sat)\n")
day=int(input("Enter the starting day of the month(0-6) to generate the calender : "))
l=['Sun','Mon','Tue','Thu','Fri','Sat']
print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
print("-----------------------------------------------------")
one=['january','march','may','july','october','december']
zero=['april','june','august','september','november']
c=0
p=0
i=0
if month in one:
    while(i<=8):
        if(i<day):
            print(" ",end="\t")
            c+=1
        else:
            for j in range(1,32):
                if(c==7):
                    print()
                    c=0
                print(j,end="\t")
                c+=1
            break
        i+=1
    print()
elif month in zero:
    while(i<=8):
        if(i<day):
            print(" ",end="\t")
            c+=1
        else:
            for j in range(1,31):
                if(c==7):
                    print()
                    c=0
                print(j,end="\t")
                c+=1
            break
        i+=1
    print()
elif month=='february':
    while(i<=8):
        if(i<day):
            print(" ",end="\t")
            c+=1
        else:
            for j in range(1,29):
                if(c==7):
                    print()
                    c=0
                print(j,end="\t")
                c+=1
            break
        i+=1
else:
    print("Enter the name correctly!!!")
                
                