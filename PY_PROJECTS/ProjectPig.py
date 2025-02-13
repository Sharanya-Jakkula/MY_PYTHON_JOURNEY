#pig project
import random
#dice
def roll():
    roll=random.randint(1,6)
    return roll
#winner
def win():
    if(max(scores)>=50):
        l=scores.index(max(scores))
        print(f'Player {l+1} is the Winner!!!\nCongratulations....') 
#input
num=input("Enter the number of players(2-4) : ")
if(num.isdigit()):
    num=int(num)
    if(num<=4 and num>=2):
        scores=[0 for i in range(num)]
        while(max(scores)<=50):
            for j in range(num):
                print(f'It\'s player{j+1} turn ')
                choice=input('Do you wanna roll the dice : (y or n)')
                if(choice.lower()!='y'):
                    print('dice passed on!!!')
                    continue
                else:
                    dice=roll()
                    scores[j]+=dice
                    print(f'Dear player{j+1}!!!Your rolled {dice} and your current score is {scores[j]}') 
                    win()
    else:
        print('The number of players is crossing the limit\nWe are Sorry!!!')
else:
    print("Sorry!!!Wrong input")
    
    