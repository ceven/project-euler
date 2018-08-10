# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from prime_util.prime_util import *


def p3(n):
    for i in range(n / 2, 2, -1):
        if n % i == 0 and is_prime_number(i):
            return i
    return None


def p3_optimised(n):
    prime_factors = prime_decomposition(n)
    return max(prime_factors)


n = 600851475143
# n = 13195

print p3_optimised(n)

