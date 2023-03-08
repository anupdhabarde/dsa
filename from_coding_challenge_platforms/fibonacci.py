"""
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. 
That is,

    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).


Example 1:

    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.


Example 2:

    Input: n = 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Example 3:

    Input: n = 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

    0 <= n <= 30
"""


from functools import cache


class Solution:
    def iterative_fib(self, n: int) -> int:
        """
        Iterative solution

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n in [0, 1]:
            return n

        last_fib_number = 0
        current_fib_number = 1

        for _ in range(2, n + 1):
            current_fib_number, last_fib_number = (
                current_fib_number + last_fib_number,
                current_fib_number,
            )

        return current_fib_number

    def recursive(self, n: int) -> int:
        """
        Recursive Solution

        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        if n in [0, 1]:
            return n

        return self.recursive(n - 1) + self.recursive(n - 2)

    @cache
    def recursive_cached(self, n: int) -> int:
        """
        Recursive Solution (Cached)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n in [0, 1]:
            return n

        return self.recursive_cached(n - 1) + self.recursive_cached(n - 2)

    def recursive_list_cache(self, n: int, notebook=None) -> int:
        """
        Recursive Solution (Dynamic Programming)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if notebook is None:
            notebook = [None] * (n + 1)

        if not notebook[n]:
            if n in [0, 1]:
                notebook[n] = n  # type: ignore
            else:
                notebook[n] = self.recursive_list_cache(  # type: ignore
                    n - 1, notebook
                ) + self.recursive_list_cache(n - 2, notebook)

        return notebook[n]  # type: ignore


if __name__ == "__main__":
    solution = Solution()
    assert solution.iterative_fib(69) == 117669030460994
    assert solution.recursive(30) == 832040
    assert solution.recursive_cached(69) == 117669030460994
    assert solution.recursive_list_cache(69) == 117669030460994
