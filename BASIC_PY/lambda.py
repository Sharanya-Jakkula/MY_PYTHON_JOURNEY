#to demonstrate the functioning of the lambda expressions
sum=lambda x,y: x+y
print(sum(10,20))
#lambda functions cannot access global variables
'''
def increment(y):
    return lamda y:y+1
    
def func(f,n):
    return f(n)
twice=lamda x :x**2
func(twice,10)
lambda functions can also call other functions

'''