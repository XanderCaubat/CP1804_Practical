"""
CP1404/CP5632 Practical
SilverServiceTaxi Test, derived from Car
Xander Dino Caubat
"""

from Practicals.prac08.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Hummer", 100, 2)
    silver_service_taxi.drive(100)
    print(silver_service_taxi)
    print(silver_service_taxi.get_fare())


main()