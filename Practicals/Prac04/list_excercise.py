"""
CP1404 - Practicals
1. Basic list operations
2. Woefully inadequate security checker
"""

# 1. Basic list operations

# MIN = 0
# MAX = 5
# numbers = []
#
#
# def main():
#     get_number()
#     average = get_average()
#     print("The first number is {:,.0f}".format(numbers[MIN]))
#     print("The last number is {:,.0f}".format(numbers[MAX - 1]))
#     numbers.sort()
#     print("The smallest number is {:,.0f}".format(numbers[MIN]))
#     print("The largest number is {:,.0f}".format(numbers[MAX - 1]))
#     print("The average of the numbers  is {}".format(average))
#
#
# def get_average():
#     total = sum(numbers)
#     average = total / len(numbers)
#     return average
#
#
# def get_number():
#     for i in range(MIN, MAX):
#         number = float(input("Number: "))
#         numbers.append(number)
#
#
# main()


# 2. Woefully inadequate security checker


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    get_username()


def get_username():
    username = input("Username: ")
    while username != '':
        if username in usernames:
            print("Access Granted.")
            username = input("Username: ")
        else:
            print("Access Denied")
            username = input("Username: ")



main()
