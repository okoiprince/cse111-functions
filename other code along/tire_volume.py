"""
Author: Prince Francis Okoi

Purpose: Program reads from the keyboard the three numbers for a tire then computes and outputs the volume of space inside that tire and write input to volume.txt

Extra creativity on line 20 and 40 program writes the day of the week to file volume.txt 
Extra creativity on line 34 and 42 to 50, Ask the user if she wants to buy tires with the dimensions that she entered then get phone number and add to file volume.txt. 

"""
import math
from datetime import datetime

#Constants
PI = math.pi
DENOMINATOR = 10000000000

#Get the current date and day
current_date = datetime.now()
date = current_date.strftime("%Y/%m/%d")
day = current_date.strftime("%A")

#Prompt for three numbers and convert
width = float(input("Enter the width of the tire in mm (ex 205): " ))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

#Calculate the Volume of Tire
numerator = PI * width**2 * ratio * (width * ratio + 2540 * diameter)
volume = numerator / DENOMINATOR

#Display volume of tire 
print(f"The approximate volume is {volume:.2f} liters \n")

#Ask the user if she wants to buy tires with the dimensions that she entered
option = str(input("Do you want to buy tire? (yes / no): ").lower())

#Program Appends to volumes.txt file
with open("volume.txt", "a") as filename:
    #Write to Volume.txt
    filename.write(f"{date}, {day}, {width}, {ratio}, {diameter}, Tire volume: {volume:.2f}\n")

    #Extra creativity append phone number to file 
    if option == "yes":
        phone = str(input("Enter phone number: "))
        filename.write(f"Phone number: {phone} \n")
    elif option == "no":
        print("Thank you")
    else: 
        print("Incorrect Option")
