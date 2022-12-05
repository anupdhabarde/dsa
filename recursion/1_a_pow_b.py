"""
PROBLEM STATEMENT:
==================
    Given two numbers a & b, find the value of a^b.
    Input: a = 2; b = 3
    Output: 8
    Explanation: 2^3 = 8.
"""


def get_pow_itera(base, exponent):
    """
    Finds exponent to the power base using iteration.
    TC: O(n) where n is exponent.
    SC: O(1)
    """
    if exponent < 0:
        raise ValueError("Negative exponent is not supported.")

    result = 1
    for _ in range(exponent):
        result *= base

    return result


def get_pow_recur(base, exponent):
    """
    Finds exponent to the power base using recursion.
    TC: O(n) where n is exponent.
    SC: O(1)
    """
    if exponent < 0:
        raise ValueError("Negative exponent is not supported.")

    # base case
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    # recursive case
    return get_pow_recur(base, exponent - 1) * base


if __name__ == "__main__":
    assert get_pow_itera(2, 0) == 1
    assert get_pow_itera(2, 1) == 2
    assert get_pow_itera(2, 3) == 8
    assert get_pow_itera(2, 100) == 1267650600228229401496703205376

    assert get_pow_recur(2, 0) == 1
    assert get_pow_recur(2, 1) == 2
    assert get_pow_recur(2, 3) == 8
    assert get_pow_recur(2, 100) == 1267650600228229401496703205376
