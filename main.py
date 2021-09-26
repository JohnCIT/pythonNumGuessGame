import random

# Randomly assign the number to begin with
computerGuess = random.randint(1, 100) 
print(computerGuess)

# Start with user guess
userGuess = 0

# Make the game loop
while userGuess != computerGuess:

    # Give the user a welcome message
    print("Welcome - Guess the number! it is between 1 and 100")


    # Ask the user for there guess
    userGuess = input("What is your guess?")
    userGuess = int(userGuess)


    print(userGuess == computerGuess, userGuess, " : ", computerGuess)