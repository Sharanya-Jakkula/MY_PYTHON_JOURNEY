# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=re.compile(r'(+|-|\.)[0-9]][0.9]+')
st=input()
res=re.search(pattern,st)
if(res!=None):
    print(True)
else:
    print(False)