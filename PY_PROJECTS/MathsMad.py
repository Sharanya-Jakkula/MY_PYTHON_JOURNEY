#to frame set of questions randomly and then guess the answer
import random
def expression():
    operators=['+','-','*','**','/']
    first=random.randint(0,15)
    second=random.randint(1,5)
    op=random.choice(operators)
    exp=str(first)+op+str(second)
    return exp
print('Let us have some fun with Math!!!')
score=0
for i in range(5):
    ex=expression()
    print(ex)
    ans=input('Guess the answer : ')
    act=str(int(eval(ex)))
    if(ans==act):
        score+=1
print(f"Your score is {score}/5")
    
