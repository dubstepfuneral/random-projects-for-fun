# thought this would be fun
import random as rd
import re
def findIndex(string, letter):
    return [m.start() for m in re.finditer(letter, string)]

def getRandomLossWords():
    list = ['Bruh!', 'Brekh!', 'Wrong!', 'Wronggg!', 'Beep!', 
    'AHHHHHHH AAAAAAAAHHHHHHHHHHHH AHHHHHAHHHHHHHHHHHHHHHHHH', 
    '*dies*', "you're killing a man. im contacting fbi, you're fucked.", 'Damn Daniel!', 'Крым Наш!', 'bruh', 
    'playin minecraffft', '*slap*', 'Fuck you!', 'Stop the cap!', "you're the imposter. sus.", 'SUS!', 'CUM!',
    'BRUH! *dies*', 'hey babe *shits furiously'] 
    print(list[rd.randrange(0, len(list))])
    
with open('forHangman.txt', 'r') as file:
    wordList = file.readlines()
tries = 0
wrong = 0
word = wordList[rd.randrange(0, len(wordList))]
hangWord = "_" * (len(word)-1)
guessed = []
guess = 0
print(word)
while True:
    if tries == 0:
        print(hangWord)
    else:
        counter = 0
        reserve = hangWord
        hangWord = ""
        for i in reserve:
            if counter in guessed:
                hangWord = hangWord + word[counter]
            else:
                hangWord = hangWord + "_"
            counter += 1
        print(hangWord)

    if wrong == 1:
        print("-——————-\n|\n|\n|\n|\n|")
        getRandomLossWords()
    elif wrong == 2:
        print("-——————-\n|\n|      o\n|\n|\n|")
        getRandomLossWords()
    elif wrong == 3:
        print("-——————-\n|\n|      o\n|      |\n|\n|")
        getRandomLossWords()
    elif wrong == 4:
        print("-——————-\n|\n|      o\n|     /|\n|\n|")
        getRandomLossWords()
    elif wrong == 5:
        print("-——————-\n|\n|      o\n|     /|\\\n|\n|")
        getRandomLossWords()
    elif wrong == 6:
        print("-——————-\n|\n|      o\n|     /|\\\n|     /\n|")
        getRandomLossWords()
    elif wrong == 7:
        print("-——————-\n|\n|      o\n|     /|\\\n|     / \\\n|")
        getRandomLossWords()
    elif wrong == 8:
        print("-——————-\n|      |\n|      o\n|     /|\\\n|     / \\\n|")
        getRandomLossWords()
        print("Game over. You lost.")
        print("Tries - " + str(tries) + ", wrong guesses - " + str(wrong))
        print("The word was -", word)
        exit()
    
    if "_" not in hangWord:
        print("You won!")
        print(hangWord)
        print("Tries - " + str(tries) + ", wrong guesses - " + str(wrong))
        exit()
    
    guess = str(input("Put in your guess: "))
    if guess in word:
        guessLst = findIndex(word, guess)
        for i in guessLst:
            guessed.append(i)
        print(guessed)
    else:
        wrong += 1

    tries += 1