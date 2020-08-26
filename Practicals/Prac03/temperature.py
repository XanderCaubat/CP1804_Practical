"""CP1804 - Practicals Functions
Do-from-scratch Exercises
a. temperatures.py - use 2 functions for converting
Celsius to Fahrenheit and vice versa Important: Remember SRP - functions should do one thing, so these should be
calculation functions. Do not get user input or print output in the functions - do those outside. That means these
will be very small functions... that's OK... they abstract a core piece of functionality """


def main():
    MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    convert_temperature(MENU, choice)


def convert_temperature(MENU, choice):
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = 5 / 9 * (fahrenheit - 32)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
