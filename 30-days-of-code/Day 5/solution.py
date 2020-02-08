#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    if n < 2 or n > 20:
        raise Exception('Invalid n value')

    for multiple in range(1, 11):
        print('%d x %d = %d' % (n, multiple, n*multiple))
