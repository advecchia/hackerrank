from statistics import mean

MIN_STRING_NAME_LENGTH = 1
MAX_STRING_NAME_LENGTH = 10
MIN_SCORE_VALUE = 0
MAX_SCORE_VALUE = 100


def validate_string_name(string_name):
    if MIN_STRING_NAME_LENGTH > len(string_name) or len(string_name) > MAX_STRING_NAME_LENGTH:
        raise ValueError('String name length is invalid.')


def validate_id_len(id_number):
    if not len(str(id_number)) == 7:
        raise ValueError('ID number is lower than 7 digits')


def validate_input_numbers(test_scores):
    for score in test_scores:
        if MIN_SCORE_VALUE > score or score > MAX_SCORE_VALUE:
            raise ValueError('Invalid test score value.')


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber


    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, id_number, test_scores):
        validate_string_name(first_name)
        validate_string_name(last_name)
        validate_id_len(id_number)
        validate_input_numbers(test_scores)

        super().__init__(first_name, last_name, id_number)
        self.scores = test_scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = mean(self.scores)
        if average < 40:
            return 'T'

        elif average < 55:
            return 'D'

        elif average < 70:
            return 'P'

        elif average < 80:
            return 'A'

        elif average < 90:
            return 'E'

        else:
            return 'O'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
