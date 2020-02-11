#!/bin/python3

import math
import os
import random
import re
import sys

MIN_ARRAY_SIZE = 1
MAX_ARRAY_SIZE = 1000
LESSER_INT_VALUE = 1
GREATER_INT_VALUE = 10000


def validate_array_size(array_size):
    if MIN_ARRAY_SIZE > array_size > MAX_ARRAY_SIZE:
        raise Exception('Invalid array size number.')


def validate_integer_value(int_value):
    if LESSER_INT_VALUE > int_value > GREATER_INT_VALUE:
        raise Exception('Invalid integer value inside array.')


if __name__ == '__main__':
    n = int(input())
    validate_array_size(n)

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()

    out = ''
    for elem in arr:
        validate_integer_value(elem)
        out += str(elem) + ' '

    print(out.rstrip())
