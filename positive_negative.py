#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program gives the user if the integer is positive or negative or 0


def main():
    # this function lets user to know if the integer is positive or negative

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process
    if integer > 0:
        # output
        print("+")
    elif integer < 0:
        # output
        print("-")
    else:
        # output
        print("0")


if __name__ == '__main__':
    main()
