n = 27
guesses = 9
while(1):

    guessNo = int(input("You have " + str(guesses) + " guesses"))
    guesses-=1

    if guessNo == n:
        print("Congrats! you guessed it right " + "in guesses " + str(guesses))
        break
    elif guessNo <= 30 and guessNo >= 25:
        print("you are close keep guessing")
    elif guessNo < n:
        print("guess a greater no")
    elif guessNo > n:
        print("guess a smaller no")
    if (guesses == 0):
        print("Game Over you failed")
        break
