from random import randint

#Greet player

print("Hey. Lets play a game...Type out one of the three choices.")
print("")
#create list of play options

x = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = x[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print ("You Win!", player, "obliterates", computer )

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print ("You Win!", player, "covers", computer )

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "destroys", player)
        else:
            print ("You Win!", player, "cut", computer)

    else:
        print("That is not a valid play. Check your spelling.")

    #player was set to True, but we want it to be False os the loop continues
    player = False
    computer = x[randint(0,2)]

