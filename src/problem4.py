# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(word):
    s = len(word)
    for i in xrange(0, s / 2):
        if word[i] != word[s - i - 1]:
            return False
    return True


def p2():
    max_p = 0
    for i in range(10, 100):
        for j in range(10, 100):
            p = i*j
            if is_palindrome(str(p)) and p > max_p:
                max_p = p
    return max_p


def p():
    max_p = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i*j
            if is_palindrome(str(p)) and p > max_p:
                max_p = p
    return max_p

print is_palindrome("abba")
print is_palindrome("aca")
print is_palindrome("ad")
print is_palindrome("adc")
print p()

