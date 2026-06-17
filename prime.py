def is_prime(n):

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


def primes_upto(limit):

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")

    if limit < 2:
        return []

    prime_list = []

    for num in range(2, limit + 1):

        if is_prime(num):
            prime_list.append(num)

    return prime_list
