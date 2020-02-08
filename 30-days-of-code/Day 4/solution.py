YOU_ARE_YOUNG = 'You are young.'
YOU_ARE_A_TEENAGER = 'You are a teenager.'
YOU_ARE_OLD = 'You are old.'
INVALID_AGE = 'Age is not valid, setting age to 0.'


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.validateAge(initialAge)
        if initialAge < 0:
            print(INVALID_AGE)
            self.age = 0
        else:
            self.age = initialAge

    def validateAge(self, age):
        if age < -5 or age > 30:
            raise Exception('Invalid age value.')

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print(YOU_ARE_YOUNG)
        elif self.age < 18:
            print(YOU_ARE_A_TEENAGER)
        else:
            print(YOU_ARE_OLD)

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print('')
