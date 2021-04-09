#!/bin/python3

# This is a programme performs the collatz sequence.

# Determine collatz sequence
def collatz(_number):
    if _number % 2 == 0:
        # Even
        return _number // 2
    elif _number % 2 == 1:
        # Odd
        return 3 * _number + 1


# Check if user value is a valid integer
# Will request until true
def userInput():
    while True:
        try:
            # Ask the player to enter a number.
            myNumber = int(input('Please select any number: \n'))

            # Until value resolves to int(1) call collatz()
            while myNumber != 1:
                myNumber = collatz(myNumber)
                print(myNumber)
            break
        except ValueError:
            print('[-] Error: Number not a valid integer number.')
            print('[-] Please select a valid integer number: \n')


userInput()
