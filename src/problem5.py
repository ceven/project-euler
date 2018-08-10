# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

from prime_util.prime_util import prime_factors


def is_divisible(i, factors):
    for f in factors:
        if i % f != 0:
            return False
    return True


def p_simple():
    factors = range(2, 11)
    i = 10
    while True:
        if is_divisible(i, factors):
            return i
        i = i + factors[len(factors)-1]


def p():
    factors = range(2, 21)
    prime_count = {}
    for f in factors:
        prime_decomposition = prime_factors(f)
        prime_count_tmp = {}
        for p in prime_decomposition:
            if p in prime_count_tmp:
                prime_count_tmp[p] = prime_count_tmp[p] + 1
            else:
                prime_count_tmp[p] = 1
        for p in prime_count_tmp:
            if p not in prime_count or prime_count_tmp[p] > prime_count[p]:
                prime_count[p] = prime_count_tmp[p]

    print prime_count
    r = 1
    for p in prime_count:
        print p, prime_count[p]
        r *= math.pow(p, prime_count[p])
    return r


print p()

