"""
CP1404 - Assignment 1
Travel tracker
Xander Dino Caubat
-You are to plan and then code a console-based program in Python 3, as described in the
following information and sample output. This assignment will help you build skills using
selection, repetition, file input/output, exceptions, lists, functions and string formatting. Do not
define any of your own classes or use code constructs that haven't been taught in this
subject. Assignment 2 will build on this program with more advanced code constructs
including dictionaries, classes and a Graphical User Interface (GUI).
"""
FILENAME = "list_places.txt"
MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place visited\nQ - Quit"
MIN = 0
visited_places = []
unvisited_places = []
enum_visited_places = enumerate(visited_places)
enum_unvisited_places = enumerate(unvisited_places)


def main():
    input_file = open(FILENAME, 'r')
    get_list(input_file)
    number_of_places = get_number_of_places()
    total_place = len(visited_places)
    print("Travel tracker 1.0 - by Xander Dino Caubat")
    print("{} places loaded from {}".format(number_of_places, FILENAME))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            if len(unvisited_places) != MIN:
                print_list_of_places()
                print_total_places()
            else:
                print_list_of_places()
                print_no_places_left()
        elif choice == "A":
            place = get_new_place().title()
            country = get_country().title()
            priority = get_valid_number()
            append_to_list(country, place, priority)
            print_added_to_travel_tracker(country, place, priority)
        elif choice == "M":
            if len(unvisited_places) != MIN:
                print_list_of_places()
                print_total_places()
                print_number_input()
                mark_name()
                print_place_visited()
            else:
                print_unvisited_places()
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()
    print("{} places saved to {}".format(total_place, FILENAME))
    print("Have a nice day :)")
    write_into_file()
    input_file.close()


def print_unvisited_places():
    print("No unvisited places")


def print_number_input():
    print("Enter the number of place to mark as visited.")


def print_added_to_travel_tracker(country, place, priority):
    print("{} in {} (priority {}) added to Travel Tracker.".format(place, country, priority))


def print_no_places_left():
    print("{} places. No places left to visit. Why not add a new place?".format(get_number_of_places()))


def mark_name():
    # this will mark places.
    number = get_mark_number()
    try:
        visited_places.append(unvisited_places[number - 1])
        unvisited_places.remove(unvisited_places[number - 1])
    except IndexError:
        print("That place is already visited.")


def write_into_file():
    # this will write into file.
    output_file = open(FILENAME, 'w')
    for place in visited_places:
        output_file.write(place.strip(', v n') + ',v\n')
    output_file.close()


def print_place_visited():
    place = visited_places[len(visited_places) - 1]
    place.strip(", n v")
    parts = place.split(',')
    print("{} in {} visited!".format(parts[0], parts[1]))


def print_total_places():
    total_places = len(visited_places + unvisited_places)
    print("{} places. You still want to visit {} places.".format(total_places, len(unvisited_places)))


def append_to_list(country, place, priority):
    unvisited_places.append("{},{},{},n".format(place, country, priority))


def print_list_of_places():
    # this will print the list.
    unvisited_places.sort()
    unvisited_places.reverse()
    visited_places.sort()
    for count, line in enumerate(unvisited_places, 1):
        line.strip(", n v")
        parts = line.split(',')
        print("*", count, ".", "{:<10} in {:<11}  priority {:<3}".format(parts[0], parts[1], parts[2]))
    for count, line in enumerate(visited_places, len(unvisited_places) + 1):
        line.strip(", v n")
        parts = line.split(',')
        print(" ", count, ".", "{:<10} in {:<11}  priority {:<3}".format(parts[0], parts[1], parts[2]))


def get_list(input_file):
    for line in input_file:
        if line.endswith("v\n"):
            line = line.strip()
            parts = line.split(',')
            visited_places.append("{},{},{},v".format(parts[0], parts[1], parts[2]))
        elif line.endswith("n\n"):
            line = line.strip()
            parts = line.split(',')
            unvisited_places.append("{},{},{},n".format(parts[0], parts[1], parts[2]))


def get_number_of_places():
    # this will count the number of places.
    number_of_place = len(visited_places) + len(unvisited_places)
    return number_of_place


def get_new_place():
    new_place = input("Name: ")
    while new_place == "":
        print("Input cannot be blank.")
        new_place = input("Name: ")
    return new_place


def get_country():
    new_country = input("Country: ")
    while new_country == "":
        print("Input cannot be blank.")
        new_country = input("Country: ")
    return new_country


def get_valid_number():
    valid_number = False
    while not valid_number:
        try:
            number = int(input("Priority: "))
            if number <= 0:
                print("Number must be > 0.")
            else:
                return number
        except ValueError:
            print("Invalid input; please enter a valid number")


def get_mark_number():
    valid_number = False
    while not valid_number:
        try:
            number = int(input(">>> "))
            if number <= 0:
                print("Number must be > 0.")
            else:
                return number
        except ValueError:
            print("Invalid input; please enter a valid number")


main()
