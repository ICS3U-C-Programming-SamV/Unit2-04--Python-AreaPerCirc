#!/usr/bin/env python3
# Created By: Sam V
# Date: Sep 29th , 2026
# this program asks the user for the radius of a circle
# and calculates the area and circumference of the circle.
# Input: Get radius from the user

import math


def main():
    print("--- Circle Area & Circumference Calculator ---\n")

    # Get input radius from user (supports float/decimal inputs)
    radius_input = input("Enter the radius of the circle: ")
    radius = float(radius_input)

    # Get units for formatting output
    units = input("Enter the unit of measurement (e.g., cm, m, in): ").strip()

    # Calculate Area: A = π * r^2
    area = math.pi * (radius ** 2)

    # Calculate Circumference / Perimeter: C = 2 * π * r
    circumference = 2 * math.pi * radius

    # Display results rounded to 2 decimal places
    print("\n--- Results ---")
    print(f"Radius:        {radius} {units}")
    print(f"Area:          {area:.2f} {units}²")
    print(f"Circumference: {circumference:.2f} {units}")


if __name__ == "__main__":
    main()
