# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
import math


def p(x):
    sum_square = 0
    square_sum = 0
    for i in range(1, x+1):
        sum_square += math.pow(i, 2)
        square_sum += i
    square_sum = math.pow(square_sum, 2)
    return square_sum - sum_square


print p(100)

