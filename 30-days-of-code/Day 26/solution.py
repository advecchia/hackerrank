from datetime import date

MIN_DAY_VALUE = 1
MAX_DAY_VALUE = 31
MIN_MONTH_VALUE = 1
MAX_MONTH_VALUE = 12
MIN_YEAR_VALUE = 1
MAX_YEAR_VALUE = 3000


def validate_input_day(day_value):
    if MIN_DAY_VALUE > day_value or day_value > MAX_DAY_VALUE:
        raise ValueError('Invalid day value.')


def validate_input_month(month_value):
    if MIN_MONTH_VALUE > month_value or month_value > MAX_MONTH_VALUE:
        raise ValueError('Invalid month value.')


def validate_input_year(year_value):
    if MIN_YEAR_VALUE > year_value or year_value > MAX_YEAR_VALUE:
        raise ValueError('Invalid year value.')


def validate_input_date(day_value, month_value, year_value):
    validate_input_day(day_value)
    validate_input_month(month_value)
    validate_input_year(year_value)


# Read returned date integers
r_day, r_month, r_year = map(int, input().split())
validate_input_date(r_day, r_month, r_year)

# Read expected date integers
e_day, e_month, e_year = map(int, input().split())
validate_input_date(e_day, e_month, e_year)

# Throws ValueError if the input values are not valid for dates using Gregorian Calendar.
returned = date(r_year, r_month, r_day)
expected = date(e_year, e_month, e_day)

# Book returned on time
if expected >= returned:
    print(0)
else:
    if r_year > e_year:
        print(10000)
    elif r_month > e_month:
        # Returned same year, fine for months
        print(500 * int(r_month - e_month))
    else:
        # Returned same month, fine for days
        # Find the difference for two dates and extract due date days
        due_date = returned - expected
        # Calculates fine for due date
        print(15 * int(due_date.days))
