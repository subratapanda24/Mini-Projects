## Snake Water Gun Game 
import random

choices = ["s", "w", "g"]

computer = random.choice(choices) #Computer's choice

you = input("Enter s for Snake, w for Water, g for Gun: ").lower() #User input

if you not in choices:# Check input
    print("Invalid input!")

else:
    print("You chose:", you)
    print("Computer chose:", computer)

    if computer == you:
        print("It's a Draw!")

    elif (you == "s" and computer == "w") or \
         (you == "w" and computer == "g") or \
         (you == "g" and computer == "s"):
        print("You Win!")

    else:
        print("You Lose!")

