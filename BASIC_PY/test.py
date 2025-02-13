a=['x']
b=[a,'y','z']
c=a
d=a.copy()
#on copying id changes while on assigning id remains the same
if (id(d)==id(a)):
    print(True)
else:
    print(False)
print(b)