# this is rock pepa scissoir. the classic.
import random as rd
from time import sleep

def getRandomTurn():
    ran = rd.randrange(1, 3+1)
    if ran == 1:
        return 'r'
    elif ran == 2:
        return 'p'
    elif ran == 3:
        return 's'


done = 0
while done == 0:
    which = input("Which one do you want? (Player vs AI - type 'p'; AI vs AI - type 'ai'): ")
    which = which.lower()
    if which != 'p' or which != 'ai':
        print("That's not 'p' or 'ai'!")
    else:
        done = 1
        break
done = 0
if which == 'p':
    while done == 0:
        print('You picked: Player VS AI')
        diff = input("Which difficulty? (Normal (AI's turn is random) - type 'normal'; Impossible (AI always wins) - type 'impossible'): ")
        if diff != 'normal' or diff != 'impossible':
            print("That's not 'normal' or 'impossible'!")
        else:
            done = 1
            break
elif which == 'ai':
    print('You picked AI vs AI')

if which == 'p':
    if diff == 'normal':
        print('n')
        
