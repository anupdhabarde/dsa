"""
https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

    Input: n = 1
    Output: true
    Explanation: 20 = 1

Example 2:

    Input: n = 16
    Output: true
    Explanation: 24 = 16

Example 3:

    Input: n = 3
    Output: false

Constraints:

    -231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def brute_force(self, n: int) -> bool:
        """
        TC: O(log n)
        SC: O(1)
        """
        if n <= 0:
            return False

        while True:
            if n == 1:
                return True
            if n % 2 == 0:
                n //= 2
            else:
                return False

    def is_power_of_two_recursive(self, n: int) -> bool:
        """
        TC: O(log n)
        SC: O(1)
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.is_power_of_two(n // 2)
        else:
            return False

    def is_power_of_two(self, n: int) -> bool:
        """
        Time Complexity:

            The bin() function has a time complexity of O(log n), as it needs to convert n to its binary representation.
            The count() method counts the occurrences of a specified substring in a string.
            In the worst case, it needs to iterate through the entire binary representation of n, which has a length of O(log n).
            Therefore, the overall time complexity is O(log n).

        Space Complexity:

            The space complexity is determined by the space used for the binary representation of n created by the bin() function.
            The space required is proportional to the length of the binary representation, which is O(log n).
            The count() method and the boolean comparison (==) do not significantly affect the space complexity.
            Therefore, the overall space complexity is O(log n).
        """
        return bin(n).count("1") == 1 if n > 0 else False


if __name__ == "__main__":
    solution = Solution()

    assert solution.brute_force(16) == True
    assert solution.brute_force(25) == False
    assert solution.brute_force(1) == True
    assert solution.brute_force(0) == False
    assert solution.brute_force(-8) == False
    assert solution.brute_force(1024) == True
    assert solution.brute_force(2049) == False
    assert solution.brute_force(-1024) == False
    assert solution.brute_force(999999999999999) == False
    assert solution.brute_force(1180591620717411303424) == True

    assert solution.is_power_of_two(16) == True
    assert solution.is_power_of_two(25) == False
    assert solution.is_power_of_two(1) == True
    assert solution.is_power_of_two(0) == False
    assert solution.is_power_of_two(-8) == False
    assert solution.is_power_of_two(1024) == True
    assert solution.is_power_of_two(2049) == False
    assert solution.is_power_of_two(-1024) == False
    assert solution.is_power_of_two(999999999999999) == False
    assert solution.is_power_of_two(1180591620717411303424) == True

    assert solution.is_power_of_two_recursive(16) == True
    assert solution.is_power_of_two_recursive(25) == False
    assert solution.is_power_of_two_recursive(1) == True
    assert solution.is_power_of_two_recursive(0) == False
    assert solution.is_power_of_two_recursive(-8) == False
    assert solution.is_power_of_two_recursive(1024) == True
    assert solution.is_power_of_two_recursive(2049) == False
    assert solution.is_power_of_two_recursive(-1024) == False
    assert solution.is_power_of_two_recursive(999999999999999) == False
    assert solution.is_power_of_two_recursive(1180591620717411303424) == True
