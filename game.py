print("Rock, Paper, Scissors, Shoot!")

import random

# Ask for a user input
# SOURCE: in-class

x = input("Please choose 'rock', 'paper', or 'scissors': ")
print (x)

 # Validate user input

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("Whoops! Please make sure you enter 'rock', 'paper', or 'scissors'")
    exit()

#Generate computer choice
#SOURCE: in-class stack overflow

valid_options = ["rock", "paper", "scissors"]

c = random.choice(valid_options)

print("You chose:", x)

print("Computer chose:", c)

#Determine winner

if (x == "rock") and (c == "scissors"):
    print("Rock beats scissors. YOU WIN!")

if (x == "scissors") and (c == "paper"):
    print("Scissors beat paper. YOU WIN!")

if (x == "paper") and (c == "rock"):
    print("Paper beats rock. YOU WIN!")


if (c == "rock") and (x == "scissors"):
    print("Rock beats scissors. Computer wins.")

if (c == "scissors") and (x == "paper"):
    print("Scissors beat paper. Computer wins")

if (c == "paper") and (x == "rock"):
    print("Paper beats rock. Computer wins.")

if (x == c):
    print ("It's a tie!")

 #Display final results
print("Play again?")
