"""
Compute mean, std, and ccdf from coin bag game.

Note:
    Could not speed up computation by factor of 10^7 necessary to compute 20!
    permutations. Closed form analytical solution for mean and std (at
    arbitrary N) is possible, but not given here.
"""
from itertools import permutations
from math import sqrt
from scipy.special import factorial


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


def get_stats(N, x=100):
    """
    Mean, std, and ccdf over all permutations

    Parameters
    ----------
    N : int
        Number of coins
    x : int, default 100
        Ccdf argument

    Returns
    -------
    mean, std, ccdf : float
    """
    perm = permutations(range(1, N + 1))
    cuml, cuml_square, idx = (0, 0, 0)
    while True:
        try:
            draw = payment(next(perm))
            cuml += draw
            cuml_square += draw ** 2
            # Count draws that exceed x
            if draw >= x:
                idx += 1
        except StopIteration:
            mean = cuml / factorial(N)
            var = cuml_square / factorial(N) - mean ** 2
            std = sqrt(var)
            ccdf = idx / factorial(N)
            return mean, std, ccdf


if __name__ == "__main__":
    N = 10
    x = 45
    mean, std, ccdf = get_stats(N, x)
    print("N:{}, mean:{}, std:{}, ccdf({}):{}".format(N, mean, std, x, ccdf))
