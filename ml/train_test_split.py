"""
API here takes in one single array at a time; i.e. repeat calls for X_data and y_data. 
rng ensures shuffling occurs on same index
"""
import numpy as np
import random


def train_test_split_0(arr, test_ratio):
    # Not sure its possible to pass a shuffled reference
    # Below is a copy
    shuffled_idxs = random.sample(range(len(arr)), len(arr))
    slice_idx = int(len(arr) * (1 - test_ratio))
    train_set = [arr[i] for i in shuffled_idxs[:slice_idx]]
    test_set = [arr[i] for i in shuffled_idxs[slice_idx:]]
    return train_set, test_set


def train_test_split_1(arr, test_ratio):
    # Simpler copy
    _arr = arr[:]
    random.shuffle(_arr)
    slice_idx = int(len(_arr) * (1 - test_ratio))
    return _arr[:slice_idx], _arr[slice_idx:]


def train_test_split_2(arr, test_ratio):
    """Slow popping"""
    _arr = arr[:]
    res = []
    train_size = int(len(arr) * (1 - test_ratio))
    while len(res) < train_size:
        idx = random.randrange(len(_arr))
        res.append(_arr.pop(idx))
    return res, _arr


def train_test_split(arr, test_ratio):
    """Shuffle `arr` input"""
    random.shuffle(arr)
    slice_idx = int(len(arr) * (1 - test_ratio))
    return arr[:slice_idx], arr[slice_idx:]


def train_test_split_np(arr, test_ratio, rng):
    # Numpy; also a copy
    shuffled_idxs = rng.permutation(len(arr))
    slice_idx = int(len(arr) * (1 - test_ratio))
    train_set = arr[shuffled_idxs[:slice_idx]]
    test_set = arr[shuffled_idxs[slice_idx:]]
    return train_set, test_set


if __name__ == "__main__":
    try:
        random.seed(42)
        rng = np.random.default_rng(42)
        # arr = [random.randrange(0, 10) for _ in range(100)]
        arr = [random.uniform(0, 10) for _ in range(10)]
        arr_y = [random.uniform(0, 10) for _ in range(10)]
        arr_np = rng.uniform(0, 1, 10)

        train_set, test_set = train_test_split_2(arr, 0.2)
        train_set_y, test_set_y = train_test_split(arr_y, 0.2)
        print(arr)
        print(arr_y)
        print(test_set)
        print(test_set_y)
        train_set_np, test_set_np = train_test_split_np(arr_np, 0.2, rng)
    # print(arr_np)
    # print(test_set_np)

    except KeyboardInterrupt:
        exit()
