#
# Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#
import math
import datetime


def p(n):
    start_time = datetime.datetime.now()
    # code
    power = str(int(math.pow(2, n)))
    sum_digits = 0
    for c in power:
        sum_digits += int(c)
    print "Program took {}".format(datetime.datetime.now() - start_time)
    return sum_digits


print p(15)
print p(1000)

