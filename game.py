print("-------------------")

import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

z = os.getenv("PLAYER_NAME")

print("Hello", z, "! Dare you attempt a round of Rock, Paper, Scissors?") # reads the variable from the environment


y = input("You decide: 'Yes' or 'No'? ")

if (y == "Yes") or (y == "yes"):
    print("Let's begin!")
else:
    print("Oh well. I live to play another day!")
    exit()
print("-------------------")
print("Rock, Paper, Scissors, Shoot!")



# Ask for a user input
# SOURCE: in-class

x = input("Please choose 'rock', 'paper', or 'scissors': ")
print (x)

 # Validate user input
 #Added options for capital letters at beginning of words for better UX (not getting kicked out of the game)

if (x == "rock") or (x == "paper") or (x == "scissors") or (x == "Rock") or (x == "Paper") or (x == "Scissors"):
    print("VALID")
else:
    print("Whoops! Please make sure you enter 'rock', 'paper', or 'scissors'. ")
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

#add capitals for human input

if (x == "rock") or (x == "Rock") and (c == "scissors"):
    print("Rock beats scissors. YOU WIN!")

elif (x == "scissors") or (x == "Scissors") and (c == "paper"):
    print("Scissors beat paper. YOU WIN!")

elif (x == "paper") or (x == "Paper") and (c == "rock"):
    print("Paper beats rock. YOU WIN!")


elif (c == "rock") and (x == "scissors") or (x == "Scissors"):
    print("Rock beats scissors. The computer wins.")

elif (c == "scissors") and (x == "paper") or (x == "Paper"):
    print("Scissors beat paper. The computer wins.")

elif (c == "paper") and (x == "rock") or (x == "Rock"):
    print("Paper beats rock. The computer wins.")

elif (x == c):
    print ("It's a tie!")
print("-------------------")
 #Display final results
print("Good game!")


