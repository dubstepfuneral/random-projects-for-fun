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

def askPlayerTurn(string, reqs):
    done = 0
    while done == 0:
        userInput = input(string)
        if userInput not in reqs:
            print("That's not what was asked for!")
        if userInput in reqs:
            done = 1
            break
    return userInput

gameLogic = { # r - rock p - paper s - scissors; rp - rock (player1) paper (player2), etc.
    'rs' : 'p1',
    'rp' : 'p2',
    'pr' : 'p1',
    'ps' : 'p2',
    'sp' : 'p1',
    'sr' : 'p2',
    'rr' : 'tie',
    'pp' : 'tie',
    'ss' : 'tie'
}

def getWinner(p1, p2):
    return gameLogic[p1+p2]

impossibleAILogic = {
    'r' : 'p',
    'p' : 's',
    's' : 'r'
}

def getAITurn(pTurn):
    return impossibleAILogic[pTurn]

dict = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}
done = 0
while done == 0:
    which = input("Which one do you want? (Player vs AI - type 'p'; AI vs AI - type 'ai'): ")
    if which != 'p' and which != 'ai':
        print("That's not 'p' or 'ai'!")
    else:
        done = 1
        break
done = 0
if which == 'p':
    while done == 0:
        print('You picked: Player VS AI')
        diff = input("Which difficulty? (Normal (AI's turn is random) - type 'normal'; Impossible (AI always wins) - type 'impossible'): ")
        if diff != 'normal' and diff != 'impossible':
            print("That's not 'normal' or 'impossible'!")
        else:
            done = 1
            break
elif which == 'ai':
    print('You picked AI vs AI')

if which == 'p':
    if diff == 'normal':
        pScore = 0
        aiScore = 0
        while pScore != 5 or aiScore != 5:
            pTurn = askPlayerTurn("Which one do you pick? (rock - 'r', paper - 'p', scissors - 's'): ", ['r', 'p', 's'])
            aiTurn = getRandomTurn()
            print("AI's turn - " + dict[aiTurn])

            outcome = getWinner(pTurn, aiTurn)
            if outcome == 'p1':
                print("You've won the round!")
                pScore += 1
            elif outcome == 'p2':
                print("AI won the round!")
                aiScore += 1
            elif outcome == 'tie':
                print('You tied!')

            if pScore == 5:
                print("You won!")
                break
            elif aiScore == 5:
                print("AI won!")
                break
    elif diff == 'impossible':
        pScore = 0
        aiScore = 0
        while pScore != 5 or aiScore != 5:
            pTurn = askPlayerTurn("Which one do you pick? (rock - 'r', paper - 'p', scissors - 's'): ", ['r', 'p', 's'])
            aiTurn = getAITurn(pTurn)
            print("AI's turn - " + dict[aiTurn])

            outcome = getWinner(pTurn, aiTurn)
            if outcome == 'p1':
                print("You've won the round!")
                pScore += 1
            elif outcome == 'p2':
                print("AI won the round!")
                aiScore += 1
            elif outcome == 'tie':
                print('You tied!')

            if pScore == 5:
                print("You won!")
                break
            elif aiScore == 5:
                print("AI won!")
                break
elif which == 'ai':
    ai1Score = 0
    ai2Score = 0
    while ai1Score != 5 or ai2Score != 5:
        sleep(1.2)
        ai1Turn = getRandomTurn()
        print("AI1's turn -", dict[ai1Turn])
        sleep(1.2)
        ai2Turn = getRandomTurn()
        print("AI2's turn -", dict[ai2Turn])
        sleep(0.8)
        
        outcome = getWinner(ai1Turn, ai2Turn)
        if outcome == 'p1':
            print("AI1 won the round!")
            ai1Score += 1
        elif outcome == 'p2':
            print("AI2 won the round!")
            ai2Score += 1
        elif outcome == 'tie':
            print("AI1 and AI2 tied!")

        if ai1Score == 5:
            print('AI1 has won!')
            break
        elif ai2Score == 5:
            print('AI2 has won!')
            break