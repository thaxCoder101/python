import random

exit  == False
user_points =0
compt_points =0

while exit == False:
    option = ["rock", "paper", "scissors"]
    user_input = input("choose rock, paper, or scissors, or exit: ")
    comp_input = random.choice(option)

    if user_input =="exit":
        print("game ended")
        exit == True

    if user_input =="rock":
        if comp_input == "rock":
            print ("ur input is rock")
            print ("computer input is rock")
            print ("it is a tie")
        elif comp_input == "paper":
            print ("ur input is rock")
            print ("computer input is paper")
            print ("computer wins")
            compt_points +=1
        elif comp_input == "scissors":
            print ("ur input is rock")
            print ("computer input is scissors")
            print ("you win")
            user_points +=1

    elif user_input =="paper":
         if comp_input == "rock":
            print ("ur input is rock")
            print ("computer input is rock")
            print ("you win")
         elif comp_input == "paper":
            print ("ur input is paper")
            print ("computer input is paper")
            print ("its a tie")
            
         elif comp_input == "scissors":
            print ("ur input is paper")
            print ("computer input is scissors")
            print ("comp win")
            compt_points +=1

    elif user_input =="scissors":
         if comp_input == "rock":
            print ("ur input is scissors")
            print ("computer input is rock")
            print ("comp win")
            compt_points += 1
         elif comp_input == "paper":
            print ("ur input is scissors")
            print ("computer input is paper")
            print ("you win")
            user_points += 1
            
         elif comp_input == "scissors":
            print ("ur input is scissors")
            print ("computer input is scissors")
            print ("its a tie")

    elif user_input != "rock" or user_input != "paper" or user_input !="scissors":
        print("invalid input")

            