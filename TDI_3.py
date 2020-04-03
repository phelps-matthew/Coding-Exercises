from itertools import permutations
import numpy as np
from scipy.special import factorial
from math import sqrt


def payment(a):
    """
    Payment from one draw permutation

    Parameters
    ----------
    a : tuple of int

    Returns
    -------
    total : int
    """
    total = a[0]
    for i in range(len(a) - 1):
        total += abs(a[i + 1] - a[i])
    return total


def mean_std(N, x):
    """
    Mean from all permutations

    Parameters
    ----------
    N : int
        Number of coins

    Returns
    -------
    mean : float
    """
    perm = permutations(range(1, N + 1))
    cuml, cuml_square, idx = 0, 0, 0
    while True:
        try:
            draw = payment(next(perm))
            cuml += draw
            cuml_square += draw ** 2
            if draw >= x:
                idx += 1
        except StopIteration:
            mean = cuml / factorial(N)
            var = cuml_square / factorial(N) - mean ** 2
            std = sqrt(var)
            cuml_x = idx/factorial(N)
            print("N: {}, mean {}:, std {}:, cuml_x {}:".format(N, mean, std, cuml_x))
            return mean, std, cuml_x

def cdf(N):
    """
    Mean from all permutations

    Parameters
    ----------
    N : int
        Number of coins

    Returns
    -------
    mean : float
    """


if __name__ == "__main__":
    import timeit
    num = 1
    N = 3
    x = 5
    tstr = "mean_std({}, {})".format(N, x)
    time = timeit.timeit(
        tstr, setup="from __main__ import mean_std", number=num
    )
    avg = time/num
    print(avg)
    print("{:e}".format(avg/factorial(N)*factorial(20)))
