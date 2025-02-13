import re
pattern=r'^[789]{1}\d{9}'
N=int(input())
#for i in range(N):
res=re.search(pattern,input())
if(res!=None):
    print('YES')
else:
    print('NO') 