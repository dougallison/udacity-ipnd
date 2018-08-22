# Udacity IPND
# Part 6 Intro to Python, Part 2
# Guess a number exercise
# Create a program in which the computer repeatedly guesses
# a number the player is thinking of until the computer
# correctly guesses the number.

def prompt(num):
    print(f"My guess: {num}")
    inp = ""
    while inp.upper() not in ['H', 'L', 'C']:
        inp = input(f"Is {num} too (H)igh, too (L)ow, or (C)orrect? ")
    return inp.upper()


def play(max):
    min = 1
    print(f"Think of a number from 1 to {max}.")
    input("When you're ready, press Enter.")

    attempts = 0
    high_guess = max
    low_guess = min
    while(True):
        attempts += 1
        guess = int((high_guess + low_guess) / 2)

        if(guess == low_guess or guess == high_guess):
            print(f"{low_guess} is too low, and " +
                  f"{high_guess} is too high! Out of guesses!")
            break

        decision = prompt(guess)
        if decision == "C":
            print(f"Computer won in {attempts} attempts!")
            return
        elif decision == "H":
            high_guess = guess
        elif decision == "L":
            low_guess = guess

    print("Thanks for playing!")


if __name__ == '__main__':
    play(1000)
