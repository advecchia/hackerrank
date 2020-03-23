#!/bin/python3

import os

MIN_NUMBER_OF_STEPS = 2
MAX_NUMBER_OF_STEPS = 10 ** 6
VALID_VALLEY_STRING = 'D'
VALID_MOUNTAIN_STRING = 'U'
SEA_LEVEL = 0


def validate_input_steps(steps):
    if MIN_NUMBER_OF_STEPS > steps or steps > MAX_NUMBER_OF_STEPS:
        raise ValueError('Invalid number of steps.')


def validate_input_path_size(steps, path):
    if not steps == len(path):
        raise ValueError('Invalid length for path.')


# Complete the countingValleys function below.
def countingValleys(n, s):
    """Count the number of valleys, that is, all times that the level is
    below sea level and returns to it.

    :param n: Number of steps
    :param s: List of steps up and down
    :return: The number of valleys
    """
    valleys_count = 0
    current_level = 0
    for path_step in s:

        if path_step == VALID_VALLEY_STRING:
            current_level -= 1
        elif path_step == VALID_MOUNTAIN_STRING:
            current_level += 1
        else:
            raise ValueError('Invalid value for path char: ' + path_step)

        if current_level == SEA_LEVEL and path_step == VALID_MOUNTAIN_STRING:
            valleys_count += 1

    return valleys_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    validate_input_steps(n)

    s = input()
    validate_input_path_size(n, s)

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')
    fptr.close()
