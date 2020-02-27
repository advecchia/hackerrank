from math import ceil
from functools import reduce


class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    __MIN_INPUT_VALUE = 1
    __MAX_INPUT_VALUE = 1000

    def divisorSum(self, n):
        self.__validateInputValue(n)
        divisors = self.__findDivisors(n)
        return reduce(lambda x, y: x + y, divisors)

    def __findDivisors(self, inputValue):
        divisors = [1]
        if inputValue == 1:
            return divisors

        limit = ceil(inputValue/2)
        for i in range(2, limit + 1):
            if inputValue % i == 0:
                divisors.append(i)
        divisors.append(inputValue)

        return divisors

    def __validateInputValue(self, inputValue):
        if self.__MIN_INPUT_VALUE > inputValue or inputValue > self.__MAX_INPUT_VALUE:
            raise ValueError('Invalid input value.')


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)