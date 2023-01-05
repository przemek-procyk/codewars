import itertools


def power(a):
    return list(itertools.chain.from_iterable(itertools.combinations(a, r) for r in range(len(a) + 1)))
