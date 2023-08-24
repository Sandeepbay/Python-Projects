#In this project , we are gonna do things.
#1. Guess the number where the user plays.
#2. Another guess the number but this time the computer guesses the number.
#Should provide the necessary feedback.

#Guess the number (Player : User)

import random
x=input("Enter the level of the game ")
a=1
b=int(x)
def guessNumber(x):
    numberToGuess=random.randint(a,b)
    #print(numberToGuess , "to be guessed")
    guess=0
    while(guess!= numberToGuess):
        guessedNumber = int(input("Guess a number "))
        if(guessedNumber<numberToGuess):
            print("Guessed number is low , Go higher")
        elif(guessedNumber>numberToGuess):
            print("Guessed number is large , Guess low")
        else:
            print("Guessed the right number")
            quit()
guessNumber(x)