print("-------------------")

##PLAYER_NAME = os.getenv(“PLAYER_NAME", default="Player One")

print("Hello 'Player One'! Dare you attempt a round of Rock, Paper, Scissors?")

y = input("You decide: 'Yes' or 'No'? ")

if (y == "Yes"):
    print("Let's begin!")
else:
    print("Oh well. I live to play another day!")
    exit()
print("-------------------")
print("Rock, Paper, Scissors, Shoot!")

import random

# Ask for a user input
# SOURCE: in-class

x = input("Please choose 'rock', 'paper', or 'scissors': ")
print (x)

 # Validate user input
 #Added capital letters as options for a better user experience (not getting kicked out of the game)

if (x == "rock") or (x == "paper") or (x == "scissors"): (#x == "Rock") or (x == "Paper") or (x == "Scissors"):
    print("VALID")
else:
    print("Whoops! Please make sure you enter 'rock', 'paper', or 'scissors'")
    exit()
print("-------------------")
#Generate computer choice
#SOURCE: in-class stack overflow

valid_options = ["rock", "paper", "scissors"]

c = random.choice(valid_options)

print("You chose:", x)

print("Computer chose:", c)

#Determine winner
print("-------------------")

if (x == "rock") and (c == "scissors"):
    print("Rock beats scissors. YOU WIN!")

if (x == "scissors") and (c == "paper"):
    print("Scissors beat paper. YOU WIN!")

if (x == "paper") and (c == "rock"):
    print("Paper beats rock. YOU WIN!")


if (c == "rock") and (x == "scissors"):
    print("Rock beats scissors. The computer wins.")

if (c == "scissors") and (x == "paper"):
    print("Scissors beat paper. The computer wins")

if (c == "paper") and (x == "rock"):
    print("Paper beats rock. The computer wins.")

if (x == c):
    print ("It's a tie!")
print("-------------------")
 #Display final results
print("Play again?")


