#!/bin/python3
import re

MIN_ROW_SIZE = 2
MAX_ROW_SIZE = 30
MAX_LENGTH_FIRST_NAME = 20
MAX_LENGTH_EMAIL_ID = 50
SEARCH_STRING = '@gmail.com'


def validate_row_size(row_size):
    if MIN_ROW_SIZE > row_size or row_size > MAX_ROW_SIZE:
        raise ValueError('Invalid returned row size.')


def is_alpha_characters_only(input_string):
    pattern = re.compile('[a-z]+')
    if pattern.match(input_string):
        return True

    return False


def validate_first_name(first_name):
    if len(first_name) > MAX_LENGTH_FIRST_NAME:
        raise ValueError('Invalid first name length.')

    if not is_alpha_characters_only(first_name):
        raise ValueError('first name string contains invalid characters.')


def is_valid_email(email_id):
    # Not a real email case right?
    pattern = re.compile('[a-z@.]+')
    if pattern.match(email_id):
        return True

    return False


def validate_email_id(email_id):
    if len(email_id) > MAX_LENGTH_EMAIL_ID:
        raise ValueError('Invalid email ID length.')

    if not is_valid_email(email_id):
        raise ValueError('email ID string contains invalid characters.')


if __name__ == '__main__':
    N = int(input())
    validate_row_size(N)
    output = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        validate_first_name(firstName)

        emailID = firstNameEmailID[1]
        validate_email_id(emailID)

        if SEARCH_STRING in emailID:
            output.append(firstName)

    output.sort()
    print('\n'.join(output))
