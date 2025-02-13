#to print the square pattern
n=int(input("Enter the size of the pattern : "))
'''
c=0
for i in range(n):
    for j in range(n):
        if(j==c):
            print('$',end=" ")
        elif i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    c+=1
    print()
$ * * * * 
* $     * 
*   $   * 
*     $ * 
* * * * $ 
'''
#empty square pattern
'''
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
#cross dollar pattern
c=0
p=n-1
for i in range(n):
    for j in range(n):
        if(j==c or j==p):
            print('$',end=" ")
        elif i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    c+=1
    p-=1
    print()
    '''
$ * * * * * $ 
* $       $ * 
*   $   $   * 
*     $     * 
*   $   $   * 
* $       $ * 
$ * * * * * $ 
    '''