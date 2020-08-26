"""CP1804 - Practicals Functions
Do-from-scratch Exercises
b. broken_score.py - main should ask the user for their score and print the result.
write a new function that takes in the user's score as a parameter and returns the result to be printed. The function
should not print it.
c. Now add a new part to the bottom of broken_score's main function that generates a random
score and prints the result. If you've written your function properly, you can see that the function can be used in
different ways, e.g. without user input.
"""
import random

MIN_SCORE = 0
MAX_SCORE = 100


def main():
    score = float(input("Enter score: "))
    random_number = get_random_number()
    get_valid_score(score)
    get_random_score(random_number)
    print(get_valid_score(score))
    print(f"Random score is: {random_number}")
    print(get_random_score(random_number))


def get_random_number():
    # this will generate a random number.
    random_number = random.randint(MIN_SCORE, MAX_SCORE)
    return random_number


def get_valid_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_score(random_number):
    # this will generate score based on random number.
    if random_number < 0 or random_number > 100:
        return "Invalid score"
    elif random_number >= 90:
        return "Excellent"
    elif random_number >= 50:
        return "Passable"
    else:
        return "Bad"


main()
