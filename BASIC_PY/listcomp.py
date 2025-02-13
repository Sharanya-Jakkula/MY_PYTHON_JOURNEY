l=[i for i in range(0,10)]
print(l)
li=[i for i in range(0,10) if i%2==0]
print(li)
odd=[i for i in range(0,10) if i%2!=0]
print(odd)
oddeven=[i if i%2==0 else 'odd' for i in range(0,10)]
print(oddeven)
