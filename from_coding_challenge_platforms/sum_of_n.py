"""
Given a number n, find sum of first n natural numbers. To calculate the sum, use a recursive function.

Constraints

1 <= N <= 100
"""


class Solution:
    def sum_of_n(self, n: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 1:
            return n

        return n + self.sum_of_n(n - 1)


if __name__ == "__main__":
    solution = Solution()
    assert solution.sum_of_n(10) == 55
