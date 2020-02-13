#!/bin/python3

import math
import os
import random
import re
import sys

MIN_INPUT_NUMBER = 2
MAX_INPUT_NUMBER = 12


def validate_input_number(number):
    if MIN_INPUT_NUMBER > number or number > MAX_INPUT_NUMBER:
        raise ValueError('Invalid value for input number')


# Complete the factorial function below.
def factorial(value):
    if value <= 1:
        return 1
    else:
        return value * factorial(value - 1)


if __name__ == '__main__':
    n = int(input())
    validate_input_number(n)

    result = factorial(n)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(result) + '\n')
    fptr.close()
