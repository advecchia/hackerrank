MIN_INPUT_LENGTH = 1
MAX_INPUT_LENGTH = 10
MIN_ELEMENT_INTEGER = 1
MAX_ELEMENT_INTEGER = 100


class Difference:

    def __init__(self, a):
        self.__elements = a

    def validateElementValue(self, number):
        if MIN_ELEMENT_INTEGER > number or number > MAX_ELEMENT_INTEGER:
            raise ValueError('Invalid element value: ' + str(number))

    def computeDifference(self):
        length = len(self.__elements)
        if MIN_INPUT_LENGTH > length or length > MAX_INPUT_LENGTH:
            raise ValueError('Invalid elements list length.')

        temp_list = list(self.__elements)
        self.maximumDifference = -9999999
        for i in range(0, length - 1):
            a = self.__elements[i]
            self.validateElementValue(a)

            temp_list.pop(0)
            for b in temp_list:
                self.validateElementValue(b)
                difference = abs(a - b)

                if self.maximumDifference < difference:
                    self.maximumDifference = difference


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
