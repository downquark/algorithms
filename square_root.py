from math import floor
def sqrt(S):
    """Given an integer, return the square root.

    A continued fraction expansion implementation.
        https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

        Args:
            S: Any natural number
    """
    i = 0
    j = 1
    if S == 0 or S == 1: return S
    while j < S:
        if i ** 2 == S:
            return i
        j = j * 2
        i += 1
    k = 2 ** int(floor((i-1)/2))
    while (k ** 2) <= S:
        if k ** 2 == S:
            return k
        k += 1
    return __continued_fraction(S, [k], 1, 0)

def __continued_fraction(S, a, d_n, m_n):
    n = len(a) - 1
    m_1 = (d_n * a[n]) - m_n
    d_1 = (S - m_1 ** 2)/d_n
    a_1 = int(floor((a[0] + m_1)/d_1))
    a.append(a_1)
    if a_1 != 2 * a[0] and len(a) < 11:
        return __continued_fraction(S, a, d_1, m_1)
    else:
        result = 1.0
        while len(a):
            result = a.pop() + (1 / result)
        return result