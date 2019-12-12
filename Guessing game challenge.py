# Guessing Game Challenge
# Let's use while loops to create a guessing game.
# The Challenge:
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#   1-If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#   2-On a player's first turn, if their guess is
#       -within 10 of the number, return "WARM!"
#       -further than 10 away from the number, return "COLD!"
#   3-On all subsequent turns, if a guess is
#       -closer to the number than the previous guess return "WARMER!"
#       -farther from the number than the previous guess, return "COLDER!"
#   4-When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided.
# Good luck!

# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
import random

num = random.randint(1, 101)
print(num)

# Next, print an introduction to the game and explain the rules
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

# Create a list to store guesses
guesses = [0]

# Write a `while` loop that compares the player's guess to our number. If the player guesses correctly, break from
# the loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.

while True:
    # If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
    guess = int(input('what number are you thinking: '))
    if guess < 1 or guess > 100:
        print('Out of BOUND, please try some other number!')
        continue
    # here we compare the player's guess to our number
    if guess == num:
        print(f'congratulations you guessed correct number in {len(guesses)} attempts')
        break
    # if guess is incorrect, add guess to the list
    guesses.append(guess)

    if guesses[-2] == 0:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    else:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')