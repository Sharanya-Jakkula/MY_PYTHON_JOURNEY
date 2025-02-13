from itertools import groupby
st=input()
x=lambda i:st.count(i)
l=[(i,x(i)) for i in st]
b=[]
for i in l:
    if i not in b:
        print(i)