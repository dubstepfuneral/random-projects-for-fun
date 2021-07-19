# i'll push this to git just because for fun. im 13 as im typing this. python is kinda fun, i currently 
# know python, java, c#.
# kinda wanna maybe once find this and look back what at what i was doing at 13 except being actually really 
# good at minecraft (not my opinion), content creation, editing and being a child.
# also im russian so i learnt english almost by myself, english class at school helped a bit, but not as 
# much as le' internet.
import random as rd

def roll():
    return rd.randrange(1, 6)

num = roll()
print("—————————")
if num == 1:
    print("|       |")
    print("|   ·   |")
    print("|       |")
elif num == 2:
    print("|     · |")
    print("|       |")
    print("| ·     |")
elif num == 3:
    print("|     · |")
    print("|   ·   |")
    print("| ·     |")
elif num == 4:
    print("| ·   · |")
    print("|       |")
    print("| ·   · |")
elif num == 5:
    print("| ·   · |")
    print("|   ·   |")
    print("| ·   · |")
elif num == 6:
    print("| · · · |")
    print("|       |")
    print("| · · · |")
print("—————————")
