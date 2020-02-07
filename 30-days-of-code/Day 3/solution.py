#!/bin/python3

import math
import os
import random
import re
import sys

WEIRD = 'Weird'
NOT_WEIRD = 'Not Weird'

if __name__ == '__main__':
    n = int(input())

    if 1 > n or n > 100:
        raise Exception('Invalid value for N.')

    if n % 2 != 0:
        print(WEIRD)
    elif n in range(2, 6):
        print(NOT_WEIRD)
    elif n in range(6, 21):
        print(WEIRD)
    else:
        print(NOT_WEIRD)