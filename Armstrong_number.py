#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: October 2019
# This program determines if user input is an Armstrong Number


def main():
    # This function determines if user input is an Armstrong Number
    print("Lets find out all the Armstrong numbers.")
    number_as_string = input("Enter a number you would like to check: ")
    print("")

    try:
        number_as_int = int(number_as_string)

        # need to know length of digit
        length_of_number = len(number_as_string)
        potential_armstrong_number = 0

        for single_digit_as_string in number_as_string:
            single_digit_as_int = int(single_digit_as_string)
            adding_num = single_digit_as_int**length_of_number
            potential_armstrong_number = potential_armstrong_number
            + adding_num

            # display the result
        if number_as_int == potential_armstrong_number:
            print(number_as_int, "is an Armstrong number.")
        else:
            print(number_as_int, "is not an Armstrong number.")

    except Exception:
        print("That is not an integer.")


if __name__ == "__main__":
    main()
