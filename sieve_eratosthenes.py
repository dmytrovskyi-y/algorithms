"""
Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit
"""


def sieve_eratosthenes(length: int) -> list[int]:
    """
    Finding all prime numbers up to any given limit.
    :param length: Length array
    :return: List of prime numbers
    """
    prime_numbers = [True] * length
    prime_numbers[0] = prime_numbers[1] = False

    for i in range(2, length):
        if prime_numbers[i]:
            for f in range(2*i, length, i):
                prime_numbers[f] = False

    return [index for index, t in enumerate(prime_numbers) if t]
