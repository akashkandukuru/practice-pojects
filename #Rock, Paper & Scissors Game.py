#Rock, Paper & Scissors Game

import random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?:  ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("player: ",player)
        print("Tie!")
    
    elif player == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("player: ",player)
            print("You Loose!")

        if computer == "scissors":
            print("Computer: ",computer)
            print("player: ",player)
            print("You Win!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("player: ",player)
            print("You Loose!")
        
        if computer == "paper":
            print("Computer: ",computer)
            print("player: ",player)
            print("You Win!")

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":    
        break

print("Thanks for Playing!")


    





