"""
CP1404/CP5632 Practical
UnreliableCar Test, derived from Car
Xander Dino Caubat
"""

from Practicals.prac08.unreliable_car import UnreliableCar


def main():
    bad_car = UnreliableCar("Cheap", 100, 23)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    print(bad_car)


main()
