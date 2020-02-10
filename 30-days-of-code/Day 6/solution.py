MINIMUM_T_NUMBER = 1
MAXIMUM_T_NUMBER = 10
SMALLER_STRING = 2
GREATER_STRING = 10000


def validate_test_case_number(test_case_number):
    if MINIMUM_T_NUMBER > test_case_number > MAXIMUM_T_NUMBER:
        raise Exception('Invalid test case number.')


def validate_string(input_string):
    if SMALLER_STRING > len(input_string) > GREATER_STRING:
        raise Exception('Invalid string length.')


if __name__ == '__main__':
    # Test case number
    t_number = int(input())
    validate_test_case_number(t_number)

    for i in range(0, t_number):
        # Read test string
        s = str(input())
        validate_string(s)

        even = ''
        odd = ''
        for j in range(0, len(s)):
            if j % 2 == 0:
                even += s[j]
            else:
                odd += s[j]

        print('%s %s' % (even, odd))

