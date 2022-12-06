"""
PROBLEM STATEMENT:
==================
    Write a program to find the factorial of a given number.
        Input: n = 4
        Output: 24
        Explanation: Factorial(4) = 4*3*2*1 = 24.
"""


def get_fact_itera(num):
    """
    Finds the factorial of the number num using iteration.
    TC: O(n) where n is num.
    SC: O(1)
    """
    if num < 0:
        raise ValueError("Negative num is not supported.")

    result = 1
    for x in range(1, num + 1):
        result *= x

    return result


def get_fact_recur(num):
    """
    Finds the factorial of the number num using recursion.
    TC: O(n) where n is num.
    SC: O(1)
    """
    if num < 0:
        raise ValueError("Negative num is not supported.")

    # base case
    if num in [0, 1]:
        return 1

    # recursive case
    return num * get_fact_recur(num - 1)


if __name__ == "__main__":
    assert get_fact_itera(0) == 1
    assert get_fact_itera(1) == 1
    assert get_fact_itera(4) == 24
    assert get_fact_itera(25) == 15511210043330985984000000

    assert get_fact_recur(0) == 1
    assert get_fact_recur(1) == 1
    assert get_fact_recur(4) == 24
    assert get_fact_recur(25) == 15511210043330985984000000
