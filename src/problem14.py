#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
import math
import datetime


def collatz(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1


def chain_length_collatz(n):
    chain_length = 1
    while n > 1:
        n = collatz(n)
        chain_length += 1
    return chain_length


def chain_length_collatz_memorized(n, memory):
    chain_length = 0
    while n > 1:
        if n in memory:
            chain_length += memory[n]
            return chain_length
        n = collatz(n)
        chain_length += 1
    return chain_length + 1


def p(n):
    start_time = datetime.datetime.now()
    max_length = 0
    collatz_number = -1
    mem = {}
    for i in range(1, n):
        mem[i] = chain_length_collatz_memorized(i, mem)
        if mem[i] > max_length:
            max_length = mem[i]
            collatz_number = i
    print "Program took {}".format(datetime.datetime.now() - start_time)
    return max_length, collatz_number


print p(1000000)

