import random
key=random.randint(1,100)
print(key)
guess=int(input("Guess the number (0-100) "))
while(True):
    if (guess==key):
        print("-----------------------------------------------------")
        print(f"Hey ! you have guessed the number {guess}\nCongo ")
        print("-----------------------------------------------------")
        break
    elif (guess<key):
        print("The guess is less than the key ")
    else:
        print("The guess is greater  than the key ")
    guess=int(input("Guess the number(0-100) : "))

