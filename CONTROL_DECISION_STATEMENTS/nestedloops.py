n=int(input())
'''for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()'''

[print() if (j>=i) else print(i,end=' ') for i in range(1,n) for j in range(i+1)]
for i in range(n+1):
    for j in range(i+1):
        if (j<=i-1):
            print(i,end='')
        else:
            print()
