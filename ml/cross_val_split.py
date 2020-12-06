"""
API here takes in one single array at a time; i.e. repeat calls for X_data and y_data.
fixed seed ensures shuffling occurs on same index
"""
import numpy as np
import random


def cross_val_split(arr, k, shuffle=False):
    _arr = arr[:]
    if shuffle:
        random.shuffle(_arr)
    cut = len(_arr) // k
    folds = [_arr[i * cut: (i + 1) * cut] for i in range(k)]
    return folds


def cross_val_split_1(arr, k):
    datasets = []
    _arr = list(arr)
    fold_size = len(arr) // k
    for _ in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(_arr))
            fold.append(_arr.pop(index))
        datasets.append(fold)
    return datasets


def cross_val_split_np(arr, k, rng, shuffle=False):
    if shuffle:
        idxs = rng.permutation(len(arr))
    else:
        idxs = np.arange(len(arr))
    cut = len(arr) // k
    folds = np.array([arr[idxs[i * cut: (i + 1) * cut]] for i in range(k)])
    return folds


if __name__ == "__main__":
    try:
        random.seed(42)
        rng = np.random.default_rng(42)
        # arr = [random.randrange(0, 10) for _ in range(100)]
        arr = [random.randrange(0, 10, 1) for _ in range(10)]
        arr_np = rng.uniform(0, 1, 10)

        folds = cross_val_split(arr, 3)
        folds_np = cross_val_split_np(arr_np, 3, rng, True)
        print(arr_np)
        print(folds_np)

    except KeyboardInterrupt:
        exit()
