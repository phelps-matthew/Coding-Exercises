def _binary_search_1(arr, target, low, high):
    """Recursive w/ low, high"""
    if low > high:
        return

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return _binary_search_1(arr, target, low, mid - 1)
    else:
        return _binary_search_1(arr, target, mid + 1, high)


def binary_search_1(arr, target):
    """Recursive wrapper"""
    if arr[0] > target or arr[-1] < target:
        return
    elif arr[0] == target:
        return 0
    elif arr[-1] == target:
        return len(arr) - 1
    else:
        return _binary_search_1(arr, target, 0, len(arr) - 1)


def binary_search_2(arr, target):
    """Recursive, slicing"""
    if not arr:
        return

    mid = len(arr) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_2(arr[:mid], target)
    else:
        return binary_search_2(arr[mid + 1 :], target)


def binary_search_3(arr, target):
    """Iterative"""
    low = 0
    high = len(arr)

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_4(arr, target):
    """Iterative, slicing"""
    _arr = arr[:]

    while _arr:
        mid = len(_arr) // 2
        if _arr[mid] == target:
            return mid
        elif _arr[mid] > target:
            _arr = _arr[:mid]
        else:
            _arr = _arr[mid + 1 :]

    return None


if __name__ == "__main__":
    try:
        print(binary_search_1([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2)
        print(binary_search_1([2, 3, 4, 5, 6, 7, 8], 0) == None)
        print(binary_search_2([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2)
        print(binary_search_3([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2)
        print(binary_search_4([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2)

    except KeyboardInterrupt:
        exit()
