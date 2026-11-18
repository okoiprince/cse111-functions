"""
Author: Prince Francis Okoi
Purpose: Can Storage Efficiency Calculation

Creative addition: 
"""
import math
#constants
PI = math.pi

#main function
def main():
    name = str(input("Can name: "))
    radius = float(input("Please enter the radius of the can: "))
    height = float(input("Please enter the height of the can: "))

    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(radius, height)

    print(f"Volume of can: {volume:.2f}")
    print(f"Surface area of can: {surface_area:.2f}")
    print(f"Storage efficiency of can: {storage_efficiency:.2f}")

#function definition 
def compute_volume(radius, height):
    can_volume= PI * radius**2 * height
    return can_volume

def compute_surface_area(radius, height):
    can_surface_area= 2 * PI * radius * (radius + height)
    return can_surface_area

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    
    storage_efficiency = volume / surface_area

    return storage_efficiency

if __name__=="__main__":
    main()