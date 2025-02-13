n = int(input())
s = set(input().split())
N=int(input())
for i in range(N):
    l=input().split()
    if (l[0]=='pop'):
        s.pop()
    elif (l[0]=='remove'):
        if l[1] in s:
            s.remove(l[1])
    elif(l[0]== 'discard'):
        s.discard(l[1])
    #l=[]
sum=0
s=set(map(int,s))
#print(s)
for i in s:
    sum=sum+i
print(sum)
    
    