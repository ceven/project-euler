
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_multiples_3_or_5_below_1000():
    sum = 0
    for i in range(0,1000):
        if is_multiple(i, 3) or is_multiple(i, 5):
            sum += i
    return sum


def is_multiple(val, n):
    return val % n == 0


print sum_multiples_3_or_5_below_1000()

