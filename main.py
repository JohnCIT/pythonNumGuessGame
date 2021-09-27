import random
from user_input import getUserInput

# Randomly assign the number to begin with
computerGuess = random.randint(1, 100) 
print(computerGuess)

# Start with user guess
userGuess = 0

# Start score with 0
score = 100 

# Give the user a welcome message
print("Welcome - Guess the number! it is between 1 and 100")

# Make the game loop
while userGuess != computerGuess:    

    # Ask the user for there guess
    userGuess = getUserInput("What is your guess?\n\n")

    # Check if guess matches
    if userGuess == computerGuess:
        print("Well done! You win.\n Your score was: ", score)
    else:
        print("Wrong! Try again!")
        score = score - 1