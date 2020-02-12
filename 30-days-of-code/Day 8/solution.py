#!/bin/python3

MIN_TEST_CASE_NUMBER = 1
MAX_TEST_CASE_NUMBER = 100000
MIN_QUERY_NUMBER = 1
MAX_QUERY_NUMBER = 100000
NOT_FOUND_STRING = 'Not found'
MAX_PHONE_LENGTH = 8


def validate_test_case_number(test_case_number):
    if MIN_TEST_CASE_NUMBER > test_case_number > MAX_TEST_CASE_NUMBER:
        raise ValueError('Invalid test case number.')


def validate_query_number(query_number):
    if MIN_QUERY_NUMBER > query_number > MAX_QUERY_NUMBER:
        raise ValueError('Invalid query number.')


def validate_name(input_name):
    if not input_name.isalpha():
        raise ValueError('Input name is not alphabetic.')


def validate_phone_number(input_phone):
    if not len(input_phone) == MAX_PHONE_LENGTH:
        raise ValueError('Input phone number not contains 8 digits.')

    if not input_phone.isnumeric():
        raise ValueError('Input phone number contains non numeric characters.')


if __name__ == '__main__':
    n = int(input())
    validate_test_case_number(n)

    # read db insert values
    phone_book = dict()
    for i in range(0, n):
        name, phone_number = str(input()).split()
        validate_name(name)
        validate_phone_number(phone_number)

        phone_book[name.lower()] = phone_number

    # Read queries
    queries = 0
    try:
        while True:
            query = str(input())
            queries += 1
            validate_query_number(queries)

            try:
                validate_name(query)
                print('%s=%s' % (query.lower(), phone_book[query.lower()]))

            except KeyError:
                print(NOT_FOUND_STRING)

    except EOFError:
        # do nothing after force program to stop processing inputs: ctrl+d
        pass

    if queries == 0:
        raise Exception('Invalid query number.')
