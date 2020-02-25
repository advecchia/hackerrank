#!/bin/python3

"""
MIN_INPUT_LENGTH = 1
MAX_INPUT_LENGTH = 6

# Hacker didn't allow conditional validation for this problem, so constraints are not validated.
# Need to remove below commented code to problem pass on compiler.
def validate_input_length(input_string):
    if MIN_INPUT_LENGTH > len(input_string) or len(input_string) > MAX_INPUT_LENGTH:
        raise ValueError('Invalid input string length.')
"""


def print_input_string(input_string):
    try:
        print(int(input_string))

    except ValueError:
        print('Bad String')


S = input().strip()
# validate_input_length(S)
print_input_string(S)
