"""
CP1404/CP5632 Practical -
Test taxi
Xander Dino Caubat
"""

from Practicals.prac08.taxi import Taxi


def main():
    """Test Taxi class."""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)


main()