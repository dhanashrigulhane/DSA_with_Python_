#GAME
import random as rd
num=rd.randint(1,100)
chances=10
while chances>0:
    choice=int(input("Guess the no. between 1 to 100: "))
    if choice<num:
        print(f'You guess too LOW !!!! You have only {chances} chances left')
    elif choice>num:
        print(f'You guess too HIGH!!!! You have only {chances} chances left')
    else:
        print("CONGRATULATIONS!!!!!!!!!! BROOOOOOOOOOOO")
        break
    chances-=1