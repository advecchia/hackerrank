#!/bin/python3

MIN_CELL_VALUE = -9
MAX_CELL_VALUE = 9


def validate_cell_value(cell_value):
    if MIN_CELL_VALUE > cell_value or cell_value > MAX_CELL_VALUE:
        raise ValueError('Invalid matrix cell value.')

    return cell_value


def validate_arr_size(number_list):
    if not len(number_list) == 6:
        raise IndexError('Matrix has wrong size, need to be 6 X 6.')


if __name__ == '__main__':
    """ This program will print the hourglass sum value with have the maximum sum from a list of hourglasses extracted 
    from a 6X6 numeric matrix.
    """
    arr = []

    for _ in range(6):
        # Read next six lines from input
        numbers = input().rstrip().split()
        validate_arr_size(numbers)
        arr.append(list(map(int, numbers)))

    try:
        max_hourglass = -9999999999
        for i in range(4):
            for j in range(4):
                # Use the hourglass mask variables
                a = validate_cell_value(arr[i][j])
                b = validate_cell_value(arr[i][j+1])
                c = validate_cell_value(arr[i][j+2])
                d = validate_cell_value(arr[i+1][j+1])
                e = validate_cell_value(arr[i+2][j])
                f = validate_cell_value(arr[i+2][j+1])
                g = validate_cell_value(arr[i+2][j+2])

                sum_hourglass = a+b+c+d+e+f+g
                if sum_hourglass >= max_hourglass:
                    max_hourglass = sum_hourglass

        print(max_hourglass)

    except KeyError:
        raise ValueError('Invalid key access.')

    except IndexError:
        raise ValueError('Matrix has wrong size, need to be 6 X 6.')
