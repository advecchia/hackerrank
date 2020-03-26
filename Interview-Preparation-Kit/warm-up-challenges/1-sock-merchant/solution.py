#!/bin/python3

import os

MIN_INPUT_N_VALUE = 1
MAX_INPUT_N_VALUE = 100
MIN_INPUT_COLOR_VALUE = 1
MAX_INPUT_COLOR_VALUE = 100


def validate_input_n_value(input_n):
    if MIN_INPUT_N_VALUE > input_n or input_n > MAX_INPUT_N_VALUE:
        raise ValueError('Invalid input n value.')

    return input_n


def validate_input_color_value(input_color):
    if MIN_INPUT_COLOR_VALUE > input_color or input_color > MAX_INPUT_COLOR_VALUE:
        raise ValueError('Invalid input color value.')

    return input_color


def sockMerchant(input_n, input_ar):
    socks = {}
    pairs = 0

    for sock in input_ar:
        if sock in socks:
            del socks[sock]
            pairs += 1
        else:
            socks[sock] = 1

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = validate_input_n_value(int(input()))

    ar = list(map(validate_input_color_value, map(int, input().rstrip().split())))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
