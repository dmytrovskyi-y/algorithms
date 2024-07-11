def inversion(arr: list, length_arr: int) -> list:
    """
    Array transformations. Algorithm for rotating an array from back to front.
    :param arr: Array
    :param length_arr: Length array
    :return: Array
    """

    new_arr = [0] * length_arr
    for index in range(length_arr):
        new_arr[index] = arr[length_arr - 1 - index]

    return new_arr
