"""
Practice Problems
9. Write a Python program that creates a ParkingTicket clas for calculating the parking fee for
one vehicle
The program must:
    1. Ask the user to enter the vehicle number and parking duration in hours. 
       The duration may include a fraction, such as 2.5 hours.
    2. Calculate the fee using the billable hours:
        - Each started hour counts as one full hour, For example, 2, 1 hours is billed as 3 hours.
        - Charge 30 per billable hour for the first two hours.
        - Charge "20 for each billable hour after the first two hours.
        3. Display the vehicle number, actual parking duration, and total fee.
        4. If the duration is zero or negative, display an error message and do not calculate a fee.
        Eample: A vehicle parked for 2.5 hours is billed for 3 hours, The fee is 30 + 30+ 20 = 80.
"""
import math

class ParkingTicket:
    def __init__(self, vehicle, hours):
        self.vehicle = vehicle
        self.hours = hours

    def calculate(self):
        h = math.ceil(self.hours)

        if h <= 2:
            return h * 30
        else:
            return 60 + (h - 2) * 20

vehicle = input("Enter vehicle number: ")
hours = float(input("Enter parking hours: "))

ticket = ParkingTicket(vehicle, hours)

if hours <= 0:
    print("Invalid parking duration")
else:
    print("Vehicle Number:", vehicle)
    print("Parking Duration:", hours, "hours")
    print("Total Fee: Rs.", ticket.calculate())

