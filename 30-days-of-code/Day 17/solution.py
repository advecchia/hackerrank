import math

NON_NEGATIVE_ERROR_MESSAGE = 'n and p should be non-negative'


class Calculator:
    def __init__(self):
        pass

    def power(self, num, pw):
        if num < 0 or pw < 0:
            raise Exception(NON_NEGATIVE_ERROR_MESSAGE)

        return int(math.pow(num, pw))


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())

    try:
        ans = myCalculator.power(n, p)
        print(ans)

    except Exception as e:
        print(e)
