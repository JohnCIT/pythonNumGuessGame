# Create function to get user input and validate it
def getUserInput(message):
    userGuess = input(message)

    try:
        userGuess = int(userGuess)
    except:
        printError()

    if userGuess > 100 or userGuess < 1:
        printError()

    return userGuess     



def printError():
    print("Ensure input is numerical and between 1 and 100")


