import math


def divisors_minmax(n, dmin, dmax):
    """Find the divisors of n in the interval (dmin,dmax]."""
    i = dmin + 1
    while i <= dmax:
        if n % i == 0:
            yield i
        i += 1


def list_or_tuple(seq):
    return isinstance(seq, (list, tuple))


def flatten(seq, to_expand=list_or_tuple):
    """Flatten a nested sequence"""
    for item in seq:
        if to_expand(item):
            for subitem in flatten(item, to_expand):
                yield subitem
        else:
            yield int(item)


def mult_partitions(n, s):
    """Compute the multiplicative partitions of n of size s"""
    return [list(sorted(flatten(p), reverse=True)) for p in mult_partitions_recurs(n, s)]


def mult_partitions_recurs(n, s, pd=1):
    if s == 1:
        return [n]
    divs = divisors_minmax(n, pd, int(math.sqrt(n)))
    fs = []
    for d in divs:
        fs.extend([(d, f) for f in mult_partitions_recurs(n / d, s - 1, pd)])
        pd = d
    return fs
