# Iterative binary search implementation in a function

def binary_search(arr, target):
    """
    Iterative binary search implementation in a function
    :param arr: array to search
    :param target: target to search for
    :return: index of target in array, -1 if not found
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
