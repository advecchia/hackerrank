#!/bin/python3

MIN_TEST_CASE_SIZE = 1
MAX_TEST_CASE_SIZE = 10 ** 3
MIN_INPUT_N_LIMIT = 2
MAX_INPUT_N_LIMIT = 10 ** 3
MIN_INPUT_K_LIMIT = 2


def validate_test_case_size(tests):
    if MIN_TEST_CASE_SIZE > tests or tests > MAX_TEST_CASE_SIZE:
        raise ValueError('Invalid test case size value')


def validate_input_n_limit(input_n):
    if MIN_INPUT_N_LIMIT > input_n or input_n > MAX_INPUT_N_LIMIT:
        raise ValueError('Invalid input n value')


def validate_input_k_limit(input_k, input_n):
    if MIN_INPUT_K_LIMIT > input_k or input_k > input_n:
        raise ValueError('Invalid input k value')


def max_value(input_k, input_n):
    if ((input_k - 1) | input_k) <= input_n:
        return input_k - 1
    else:
        return input_k - 2


if __name__ == '__main__':
    t = int(input())
    validate_test_case_size(t)

    output = []
    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        validate_input_n_limit(n)

        k = int(nk[1])
        validate_input_k_limit(k, n)

        output.append(str(max_value(k, n)))

    print('\n'.join(output))
