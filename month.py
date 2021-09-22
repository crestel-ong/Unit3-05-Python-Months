#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is the Month program


def main():
    # this function displays the month a number represents

    # input
    user_number = int(input("Enter the number of a month(ex: 3 for March): "))

    # process and output
    if user_number == 1:
        print("January")
    elif user_number == 2:
        print("February")
    elif user_number == 3:
        print("March")
    elif user_number == 4:
        print("April")
    elif user_number == 5:
        print("May")
    elif user_number == 6:
        print("June")
    elif user_number == 7:
        print("July")
    elif user_number == 8:
        print("August")
    elif user_number == 9:
        print("September")
    elif user_number == 10:
        print("October")
    elif user_number == 11:
        print("November")
    elif user_number == 12:
        print("December")
    else:
        print("Invalid number")

    print("\nDone.")


if __name__ == "__main__":
    main()
