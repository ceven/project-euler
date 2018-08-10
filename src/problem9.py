#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def pythagore(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


def is_int(val):
    return val == int(val)


def p(n):
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            c = pythagore(a, b)
            if is_int(c):
                print a, b, c
                print math.pow(a, 2) + math.pow(b, 2), math.pow(c, 2)
                if a + b + c == n:
                    print a, b, c
                    return a * b * c
    return None


print p(1000)

