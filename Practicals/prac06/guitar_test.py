"""
CP1404/CP5632 Practical -
Programming language
Guitar test run
Xander Dino Caubat
"""

from Practicals.prac06.guitar import Guitar


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 7,
                                                      other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name,
                                                         False,
                                                         other.is_vintage()))


if __name__ == '__main__':
    run_tests()
