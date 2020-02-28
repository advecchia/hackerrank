#!/bin/python3

ARRAY_SORTED_MESSAGE_TEMPLATE = 'Array is sorted in %d swaps.'
FIRST_ELEMENT_MESSAGE_TEMPLATE = 'First Element: %d'
LAST_ELEMENT_MESSAGE_TEMPLATE = 'Last Element: %d'
MIN_INPUT_N_VALUE = 2
MAX_INPUT_N_VALUE = 600
MIN_INPUT_A_NUMBER = 1
MAX_INPUT_A_NUMBER = 2 * 10**6


def validate_input_n(input_n):
    if MIN_INPUT_N_VALUE > input_n or input_n > MAX_INPUT_N_VALUE:
        raise ValueError('Invalid value for input n.')


def validate_input_a_length(input_n, a_list):
    if not len(a_list) == input_n:
        raise ValueError('Invalid length for input a.')


def validate_input_a_number(a_value):
    if MIN_INPUT_A_NUMBER > a_value or a_value > MAX_INPUT_A_NUMBER:
        raise ValueError('Invalid value in input a.')


def bubble_sort_algorithm(input_n, temp_list):
    # Track number of elements swapped during a single array traversal
    num_swaps = 0
    for i in range(0, input_n):
        for j in range(0, input_n - 1):
            # Swap adjacent elements if they are in decreasing order
            if temp_list[j] > temp_list[j + 1]:
                # Do a swap in array
                temp_value = temp_list[j]
                temp_list[j] = temp_list[j + 1]
                temp_list[j + 1] = temp_value
                num_swaps += 1

        # If no elements were swapped during a traversal, array is sorted
        if num_swaps == 0:
            break

    return [num_swaps, temp_list[0], temp_list[-1]]


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
validate_input_n(n)
validate_input_a_length(n, a)

numSwaps, firstElement, lastElement = bubble_sort_algorithm(n, a)

print(ARRAY_SORTED_MESSAGE_TEMPLATE % numSwaps)
print(FIRST_ELEMENT_MESSAGE_TEMPLATE % firstElement)
print(LAST_ELEMENT_MESSAGE_TEMPLATE % lastElement)
