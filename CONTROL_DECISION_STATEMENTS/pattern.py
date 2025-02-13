#to print the pattern
n=int(input("Enter the size of the pattern : "))
#SQUARE LOOP
'''
for i in range(n):
    for j in range(n):
        print('* ',end="")
    print()
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''
#INCREASING LOOP
'''for i in range(n):
    for j in range(i+1):
        print('* ',end="")
    print() 
* 
* * 
* * * 
* * * * 
* * * * * 
'''
#DECREASING LOOP
'''
p=n+1
for i in range(n):
    p=p-1
    for j in range(p):
        print('*',end=' ')
    print()
* * * * * 
* * * * 
* * * 
* * 
* 
'''
#increasing space loop
'''
p=n+1
for i in range(n):
    p=p-1
    for j in range(p-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
#hill pattern
'''
p=n+1
for i in range(n):
    p=p-1
    for j in range(p-1):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    for l in range(i+1):
        print('*',end=' ')
    print()
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
    '''
#reverse hill pattern
'''
p=n+1
for i in range(n):
    p=p-1
    for j in range(i):
        print('  ',end="")
    for k in range(p-1):
        print('* ',end="")
    for l in range(p):
        print('* ',end="")
    print()
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
#number pattern
'''
for i in range(1,n+1):
    for j in range(n):
        print(i,end='')
    print()
11111
22222
33333
44444
55555
'''
'''
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end='')
    print()

12345
12345
12345
12345
12345
'''
#increasing number loop
'''
for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print()
1
22
333
4444
55555
'''
#number pattern
'''
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()
1
12
123
1234
12345
'''
'''
p=n+1
c=1
for i in range(1,n+1):
    p=p-1
    c=1
    for j in range(p):
        print(" ",end=" ")
    for k in range(i):
        print(c,end=" ")
        c+=1
    print()
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
        
'''
'''
#reverse hill number pattern
p=n+1
for i in range(1,n+1):
    p=p-1
    for j in range(i-1):
        print(" ",end=" ")
    for k in range(p-1):
        print(p,end=" ")
    for l in range(p):
        print(p,end=" ")
    print()
5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4 
    3 3 3 3 3 
      2 2 2 
        1 
        '''
#number hill pattern
'''
p=n
c=0
for i in range(n):
    for k in range(0,p-1):
        print(" ",end=" ")
    for j in range(i+1):
            print(j+1,end=" ")
    c=i
    for l in range(i):
            print(c,end=" ")
            c=c-1    
    print()
    p=p-1
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
'''
#tree pattern
'''
p=n
for i in range(n):
    for k in range(p-1):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end=" ")
    p-=1
    print()
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5
'''
