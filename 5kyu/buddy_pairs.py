"""
old, too slow
"""

# from math import sqrt
#
#
# def divisors_sum(n):
#     divsum = 1
#     for i in range(2, int(sqrt(n)) + 1):
#         d, m = divmod(n, i)
#         if m == 0:
#             divsum += i
#             if i != d:
#                 divsum += n // i
#     return divsum
#
#
#
# def buddy(start, limit):
#     for i in range(start, limit + 1):
#         sum_of = divisors_sum(i)
#         sum_equal_number = divisors_sum(sum_of - 1)
#         if start > sum_of:
#             continue
#         if i == (sum_equal_number - 1):
#             return [i, sum_of - 1]
#     else:
#         return "Nothing"


from math import isqrt


def sum_of_divisors(n):
    result = 1
    div = 1
    while True:
        for div in range(div + 1, isqrt(n) + 1):
            if not n % div:
                mul = 1
                while not n % div:
                    n //= div
                    mul = 1 + mul * div
                result *= mul
                break
        else:
            if n > 1:
                result *= 1 + n
            return result


def buddy(start, limit):
    def s(n):
        return sum_of_divisors(n) - n

    for n in range(start, limit + 1):
        m = s(n) - 1
        if m > n and s(m) == n + 1:
            return [n, m]
    return 'Nothing'
