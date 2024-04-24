import random

while True:
    options = ["rock","paper","scissors"]

    computer = random.choice(options)
    player = None 

    while player not in options:
        player = input("rock, paper, or scissors? ").lower()

    if player == computer:
        print ("computer: ",computer)
        print ("player: ",player)
        print ("TIE!!!")

    elif player == "rock":
        if computer == "scissors":
            print ("computer: ",computer)
            print ("player: ",player)
            print ("YOU WIN!!!")
        if computer == "paper":
            print ("computer: ",computer)
            print ("player: ",player)
            print ("YOU LOSE!!!")
    elif player == "paper":
        if computer == "rock":
            print ("computer: ",computer)
            print ("player: ",player)
            print ("YOU WIN!!!")
        if computer == "scissors":
            print ("computer: ",computer)
            print ("player: ",player)
            print ("YOU LOSE!!!")
    elif player == "scissors":
        if computer == "paper":
            print ("computer: ",computer)
            print ("player: ",player)
            print ("YOU WIN!!!")
        if computer == "rock":
            print ("computer: ",computer)
            print ("player: ",player)
            print ("YOU LOSE!!!")

    end_choice = ["yes","no"]
    play_again = None

    while play_again not in end_choice:
        play_again = input("Want to play again? (yes/no) ").lower()

    if play_again != "yes":
        break

print ("BYE!!!")
                   
            
    
