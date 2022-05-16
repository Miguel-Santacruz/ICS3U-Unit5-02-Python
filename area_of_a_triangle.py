#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program finds area of a triangle


def calculate_area(length, height):
    # calculate area

    # process
    area = (length * height) / 2

    # output
    print("The area of the triangle is {}cm²".format(area))


def main():
    # This function gets length and height

    # input
    length_as_string = input("Enter the base length of the triangle (cm): ")
    height_as_string = input("Enter the height of the triangle (cm): ")
    try:
        length = float(length_as_string)
        height = float(height_as_string)
        print("")
        if length < 0 or height < 0:
            print("Invalid input.")
        else:
            # call function
            calculate_area(length, height)
    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
