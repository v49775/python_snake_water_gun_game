#### Exercise 06  - game development -- snake-water-gun

import random

print("Welcome to the Snake , Water , Gun Game")
g_indicator=["Snake","Water","Gun"]
i=0
count = 0
counter=0
while i<=10:
    i+=1

    cPlay=random.choice(g_indicator)
    uPlay=input("Enter your choice : Snake for s, Water for w, Gun for g: ")
    print(f"Computer play: {cPlay}")
    if(uPlay=="s" and cPlay=="Water"):
        count+=1
        print("You win")

    elif (uPlay == "s" and cPlay == "Gun"):
        print("You Lose!!!")
        counter += 1

    elif (uPlay == "w" and cPlay == "Snake"):
        print("You lose!!!")
        counter += 1

    elif (uPlay == "w" and cPlay == "Gun"):
        print("You win")
        count += 1

    elif (uPlay == "g" and cPlay == "Snake"):
        print("You win")
        count += 1

    elif (uPlay == "g" and cPlay == "Water"):
        print("You lose!!!")
        counter += 1

    else:
        print("terminate this move. Beacause you and computer play same move")

if(count>counter):
    print(f"computer Win {counter} times")
    print(f"you Win {count} times")
    print("CongratulationYou are winner of this game!!!!!")
else:
    print("You loses the whole game")