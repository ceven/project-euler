#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
#
from prime_util.prime_util import *


def p(n):
    prime = 2
    prime_index = 1
    prev_primes = [prime]
    while prime_index < n:
        prime = next_prime(prime, prev_primes)
        prev_primes.append(prime)
        prime_index += 1
    return prime


print p(10001)

