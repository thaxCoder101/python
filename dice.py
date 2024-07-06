import random

def rollDice():

    diceDrawing = {
        1: {
            "___________",
            "|          |",
            "|     1    |",
            "|          |",
            "|__________|",

        },
        2: {
            "___________",
            "|          |",
            "|     2    |",
            "|          |",
            "|__________|",

        },
        3: {
            "___________",
            "|          |",
            "|     3    |",
            "|          |",
            "|__________|",

        },
        4: {
            "___________",
            "|          |",
            "|     4    |",
            "|          |",
            "|__________|",

        },
        5: {
            "___________",
            "|          |",
            "|     5    |",
            "|          |",
            "|__________|",

        },
        6: {
            "___________",
            "|          |",
            "|     6    |",
            "|          |",
            "|__________|",

        },
    }

    roll = input("roll dice (Y/N) ? ")

    

    while roll.lower() == "Y".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("dice rolled : {}".format(dice1, dice2))
        print("\n".join(diceDrawing[dice1]))
        print("\n".join(diceDrawing[dice2]))

        roll = input("roll again Y/N ??? ")

rollDice()