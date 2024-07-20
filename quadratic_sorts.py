"""
Quadratic sorting of lists (arrays), in which the worst-case execution time is Big O(N**2)
"""


def insertion_sort(arr: list) -> list:
    """
    Insertion sort array.
    Sorting execution time Big O(N**2).
    :param arr: List for sorting
    :return: Sorted list
    """
    for top in range(1, len(arr)):
        tmp = top
        while tmp > 0 and arr[tmp - 1] > arr[tmp]:
            arr[tmp], arr[tmp - 1] = arr[tmp -1], arr[tmp]
            tmp -= 1

    return arr


def choice_sort(arr: list) -> list:
    """
    Choice sort.
    Sorting execution time Big O(N**2).
    :param arr: List for sorting
    :return: Sorted list
    """
    for p in range(0, len(arr) - 1):
        for i in range(p + 1, len(arr)):
            if arr[i] < arr[p]:
                arr[i], arr[p] = arr[p], arr[i]

    return arr


def bubble_sort(arr: list) -> list:
    """
    Bubble sort array.
    Sorting execution time Big O(N**2).
    :param arr: List for sorting
    :return: Sorted list
    """
    for p in range(1, len(arr)):
        for i in range(0, len(arr) - p):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr
