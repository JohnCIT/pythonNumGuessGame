import random
from user_input import getUserInput

# Randomly assign the number to begin with
computerGuess = random.randint(1, 100) 
print(computerGuess)

# Start with user guess
userGuess = 0

# Give the user a welcome message
print("Welcome - Guess the number! it is between 1 and 100")

# Make the game loop
while userGuess != computerGuess:    

    # Ask the user for there guess
    userGuess = getUserInput("What is your guess?")

    print(userGuess == computerGuess, userGuess, " : ", computerGuess)