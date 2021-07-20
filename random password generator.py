from random import randrange
from string import ascii_lowercase

def ask(string, reqs, thatsnot):
    done = 0
    while done == 0:
        result = input(string)
        result = result.lower()
        if result in reqs:
            done = 1
            break
        else:
            print("That's not " + thatsnot + "!")
    return result

req1 = []
for i in range(6, 32+1):
    req1.append(str(i))
length = ask("What length of the password do you want? (6 to 32): ", req1, "6 to 32")
inclNum = ask("Do we include numbers? (y/n): ", ['y', 'n'], 'y/n')
inclChar = ask("Do we include characters? (y/n): ", ['y', 'n'], 'y/n')

if inclNum == 'n' and inclChar == 'n':
    charList = list(ascii_lowercase)
elif inclNum == 'y' and inclChar == 'n':
    charList = list(ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
elif inclNum == 'n' and inclChar == 'y':
    charList = list(ascii_lowercase) + ['!','@','#','$','%','^','&','*','(',')']
elif inclNum == 'y' and inclChar == 'y':
    charList = list(ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] + ['!','@','#','$','%','^','&','*','(',')']

final = ""
for i in range(0, int(length)):
    reg = randrange(0, 2)
    if reg == 0:
        final = final + charList[randrange(0, len(charList))].lower()
    if reg == 1:
        final = final + charList[randrange(0, len(charList))].upper()

print("The password:")
print(final)