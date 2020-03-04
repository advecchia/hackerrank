from math import ceil, sqrt

PRIME_MESSAGE = 'Prime'
NOT_PRIME_MESSAGE = 'Not prime'
MIN_TEST_CASE_SIZE = 1
MAX_TEST_CASE_SIZE = 30
MIN_INPUT_INTEGER = 1
MAX_INPUT_INTEGER = 2 * 10 ** 9


def validate_test_case_size(tests):
    if MIN_TEST_CASE_SIZE > tests or tests > MAX_TEST_CASE_SIZE:
        raise ValueError('Invalid test case number %d' % tests)


def validate_input_integer(input_n):
    if MIN_INPUT_INTEGER > input_n or input_n > MAX_INPUT_INTEGER:
        raise ValueError('Invalid input number %d' % input_n)


def validate_prime(number):
    # Basic case
    if number == 1:
        print(NOT_PRIME_MESSAGE)
        return

    # Basic case
    if number == 2:
        print(PRIME_MESSAGE)
        return

    # Look only into half part of numbers
    limit = ceil(sqrt(number))
    for divisor in range(2, limit + 1):
        if number % divisor == 0:
            print(NOT_PRIME_MESSAGE)
            return

    print(PRIME_MESSAGE)


test_cases = int(input())
validate_test_case_size(test_cases)

input_values = []
for i in range(0, test_cases):
    n = int(input())
    validate_input_integer(n)
    input_values.append(n)

for i in input_values:
    validate_prime(i)
