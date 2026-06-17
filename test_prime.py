import pytest
from prime import is_prime, primes_upto


def test_prime_2():
    assert is_prime(2) is True


def test_prime_7():
    assert is_prime(7) is True


def test_non_prime_8():
    assert is_prime(8) is False


def test_primes_upto_10():
    assert primes_upto(10) == [2, 3, 5, 7]


def test_primes_upto_100():

    expected = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97
    ]

    assert primes_upto(100) == expected


def test_invalid_type():
    with pytest.raises(TypeError):
        primes_upto(10.5)
