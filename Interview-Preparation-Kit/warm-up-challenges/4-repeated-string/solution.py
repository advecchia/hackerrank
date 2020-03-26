#!/bin/python3

import os

MIN_STRING_LENGTH = 1
MAX_STRING_LENGTH = 100
MIN_PREFIX_LENGTH = 1
MAX_PREFIX_LENGTH = 10**12
STRING_TO_FIND = 'a'


def validate_input_string(input_string_length):
    if MIN_STRING_LENGTH > input_string_length or input_string_length > MAX_STRING_LENGTH:
        raise ValueError('Invalid input string length.')


def validate_input_prefix(input_prefix_length):
    if MIN_PREFIX_LENGTH > input_prefix_length or input_prefix_length > MAX_PREFIX_LENGTH:
        raise ValueError('Invalid prefix length.')


def get_number_of_a_chars(string_value):
    return string_value.count(STRING_TO_FIND)


# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = get_number_of_a_chars(s)
    if a_count == 0:
        return 0

    multiplier = int(n/len(s))
    remainder = int(n % len(s))
    if multiplier < 1:
        # Takes the first n characters of input string
        return get_number_of_a_chars(s[:n])
    else:
        a_count *= multiplier
        a_count += get_number_of_a_chars(s[:remainder])
        return a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    validate_input_string(len(s))

    n = int(input())
    validate_input_prefix(n)

    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
