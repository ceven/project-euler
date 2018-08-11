import math


def is_prime(number, prev_primes):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    sqrt_number = math.sqrt(number)
    for i in prev_primes:
        if i > sqrt_number:
            return True
        if number % i == 0:
            return False
    return True


def is_prime_number(number):
    return is_prime(number, range(2, math.sqrt(number)))


def next_prime(prime, prev_primes):
    next_ = prime + 1
    while True:
        if is_prime(next_, prev_primes):
            return next_
        next_ = next_ + 1


def prime_factors(f):
    factors = []
    i = 2
    while f > 1:
        while f % i == 0:
            factors.append(i)
            f = f / i
        i = i + 1
    return factors


def primes_under(n):
    prime = 2
    prev_primes = []
    while prime < n:
        prev_primes.append(prime)
        prime = next_prime(prime, prev_primes)
    return prev_primes


def prime_decomposition(n):
    prime_factors = []
    prime_numbers = []
    remaining = n
    next_p = 2
    while remaining > 1:
        while remaining % next_p == 0:
            remaining = remaining / next_p
            prime_factors.append(next_p)
        prime_numbers.append(next_p)
        next_p = next_prime(next_p, prime_numbers)
    return prime_factors
