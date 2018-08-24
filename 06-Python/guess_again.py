# Udacity IPND
# Part 6 Intro to Python, Part 2
# Guess a number exercise
# This is an alternate version of the guessing game exercise
# in which the player tries to guess a number picked by the
# computer.

import random


def generate_number(min, max):
    return random.randint(min, max)


def evaluate_guess(guess, correct_answer):
    if(guess == None or guess == ""):
        return "N"

    guess = int(guess)
    if(guess == correct_answer):
        return "C"
    if(guess < correct_answer):
        return "L"
    if(guess > correct_answer):
        return "H"


def prompt():
    return input("What is your guess? ")


def play():
    min = 1
    max = 1000
    print(f"Welcome! Guess a number between {min} and {max}!")
    correct_answer = generate_number(min, max)
    attempts = 0
    while(True):
        guess = prompt()
        outcome = evaluate_guess(guess, correct_answer)
        attempts += 1
        if(outcome == "C"):
            print(f"You win in {attempts} attempts!")
            return

        if(outcome == "L"):
            print("Higher...guess again!")
        elif(outcome == "H"):
            print("Lower...guess again!")
        else:
            print("Thanks for playing.")
            return


play()
