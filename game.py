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
    print("Rock beats scissors. You win!")

if (x == "scissors") and (c == "paper"):
    print ("Scissors beat paper. You win!")

if (x == "paper") and (c == "rock"):
    print ("Paper beats rock. You win!")


#if (c == "rock") and (x == "scissors):
#if (c == "scissors") and (x == "paper"):
#if (c == "paper") and (x == "rock"):

 #Display final results