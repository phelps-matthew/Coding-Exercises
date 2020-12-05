def binary_search_floor(arr, target):
    """Iterative. 2[1,3]->2[1]->"""
    low = 0
    high = len(arr) - 1
    if target < arr[low]:
        return -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return high


def binary_search_ceil(arr, target):
    """Iterative. 2[1,3]->2[1]->"""
    low = 0
    high = len(arr) - 1
    if target > arr[high]:
        return -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


def binary_search_range(arr, target):
    """Return index range of target if found, else [-1, -1]"""
    idx_range = [-1, -1]
    idx_range[1] = _binary_search_range(arr, target)
    if idx_range[1] != -1:
        idx_range[0] = _binary_search_range(arr, target, upper=False)
    return idx_range


def _binary_search_range(arr, target, upper=True):
    """Return index of rightmost target value if `upper`, else leftmost"""
    key_idx = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            key_idx = mid
            if upper:
                low = mid + 1
            else:
                high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return key_idx


if __name__ == "__main__":
    try:
        print(binary_search_floor([2, 3, 5, 7, 8], 6))
        print(binary_search_ceil([2, 3, 5, 7, 8], 6))
        print(binary_search_range([2, 3, 5, 5, 5, 7, 8], 5))

    except KeyboardInterrupt:
        exit()
