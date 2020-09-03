"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
subject_list = []


def main():
    data = get_data()
    print(data)
    print(subject_list)
    display_subject_details()


def display_subject_details():
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        print("{} is taught by {:<12} and has {:>3} students".format(parts[0], parts[1], parts[2]))
    input_file.close()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_list.append(parts)
    input_file.close()


main()
