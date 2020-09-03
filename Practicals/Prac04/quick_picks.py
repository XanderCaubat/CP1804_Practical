"""
CP1404 - Practicals
Quick pick
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many
lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.
"""

import random

MIN = 1
MAX = 45
MAX_RANDOM_NUMBERS = 6


def main():
    number_of_picks = get_number_of_picks()
    for i in range(number_of_picks):
        quick_picks = []
        for j in range(MAX_RANDOM_NUMBERS):
            number = random.randint(MIN, MAX)
            while number in quick_picks:
                number = random.randint(MIN, MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))


def get_number_of_picks():
    # this will get valid number of picks
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        print("Invalid input.")
        number_of_picks = int(input("How many quick picks? "))
    return number_of_picks


main()
