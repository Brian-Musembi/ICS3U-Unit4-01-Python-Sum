#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program finds the sum of all natural numbers preceding the
#     number inputted by the user


def main():
    # this function will calculate the sum of integers between 0
    #      and a user input using a loop

    print("This program adds up all the positive integers from 0 to whatever "
          "number you input.")

    # loop counter variable
    loop_counter = 0

    # sum of positive integers variable
    numbers_sum = 0

    # input
    user_input = input("Please input a positive integer: ")
    print("")

    # process
    try:
        user_input_int = int(user_input)

        if user_input_int > 0:
            while loop_counter < user_input_int:
                numbers_sum = numbers_sum + (loop_counter + 1)
                loop_counter = loop_counter + 1
            # output
            print("The sum of all positive numbers from 0 "
                  "to {0} is {1}.".format(user_input_int, numbers_sum))
        else:
            # output
            print("{} isn't a positive integer!"
                  .format(user_input_int))
    except Exception:
        # output
        print("That isn't a number! Try again.")


if __name__ == "__main__":
    main()
