#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
import math
import datetime
from Queue import Queue

from prime_util.prime_util import primes_under


def p(n):
    start_time = datetime.datetime.now()
    primes = primes_under(n)
    print "Program took {}".format(datetime.datetime.now() - start_time)
    return sum(primes)


def improved_method_sieve_of_eratosthenes(n):
    start_time = datetime.datetime.now()
    sum_primes_under_n = 0
    is_prime = [True for i in range(0, n+1)]
    is_prime[0] = is_prime[1] = False
    for i in range(4, len(is_prime), 2):
        is_prime[i] = False
    limit = int(math.sqrt(n))
    for prime in range(3, limit + 1, 2):
        if is_prime[prime]:
            for i in range(prime*prime, len(is_prime), 2*prime):
                is_prime[i] = False

    primes_under_n = []
    for i in range(0, len(is_prime)):
        if is_prime[i]:
            primes_under_n.append(i)
    print "Program took {}".format(datetime.datetime.now() - start_time)
    print "Primes under {} are {}".format(n, primes_under_n)
    return sum(primes_under_n)


# print p(2000000)  # Answer is 142, 913, 828, 922 (>142 billion)
print improved_method_sieve_of_eratosthenes(2000000)

