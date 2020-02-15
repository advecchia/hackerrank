#!/bin/python3

import math
import os
import random
import re
import sys

MIN_INPUT_DECIMAL = 1
MAX_INPUT_DECIMAL = 1000000


def validate_input_value(input_value):
    if MIN_INPUT_DECIMAL > input_value or input_value > MAX_INPUT_DECIMAL:
        raise ValueError("Invalid n value.")


def get_one_blocks(input_value):
    """Convert input value to binary string, remove 0b from its header.
       After split the string using '0' as key.
    """
    return bin(input_value)[2:].split('0')


if __name__ == '__main__':
    n = int(input())

    validate_input_value(n)
    blocks = get_one_blocks(n)
    max_block = max(blocks, key=len)
    print(len(max_block))
