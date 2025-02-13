#to reverse a string using recursion
#-->check once
global st
def reverse(s):
    if(len(s)==0):
        return s
    else:
        return s[::-1]
        
s='boon'
res=reverse(s)
print(res)
