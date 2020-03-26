#!/bin/python3

import os

MIN_NUMBER_OF_CLOUDS = 2
MAX_NUMBER_OF_CLOUDS = 100
VALID_SAFE_CLOUD = 0


def validate_cloud_number(cloud_number):
    if MIN_NUMBER_OF_CLOUDS > cloud_number or  cloud_number > MAX_NUMBER_OF_CLOUDS:
        raise ValueError('Invalid cloud number.')


def validate_cloud_inputs(cloud_number, cloud_array_length):
    if not cloud_number == cloud_array_length:
        raise ValueError('Invalid cloud array length.')


def validate_game_start(cloud):
    if not cloud == VALID_SAFE_CLOUD:
        raise ValueError('Invalid start value for game.')


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    index = 0
    cloud_array_length = len(c) - 1

    validate_game_start(c[index])

    while True:
        if index + 2 <= cloud_array_length and c[index + 2] == VALID_SAFE_CLOUD:
            index += 2
        elif index + 1 <= cloud_array_length and c[index + 1] == VALID_SAFE_CLOUD:
            index += 1
        else:
            break

        jumps += 1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    validate_cloud_number(n)

    c = list(map(int, input().rstrip().split()))
    validate_cloud_inputs(n, len(c))

    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
