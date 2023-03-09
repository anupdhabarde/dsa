"""
Given a string, write a function that returns 1 if the given string is palindrome, else 0.
For example, "aba" is palindrome, but "abc" is not palindrome.

Input Format:
String input_str.

Constraints:
"a" <= element of input_str <= "z"

Output Format:
True / False
"""


class Solution:
    def is_palindrome(self, input_str: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(input_str) <= 1:
            return True

        return input_str[0] == input_str[-1] and self.is_palindrome(input_str[1:-1])


if __name__ == "__main__":
    solution = Solution()
    assert solution.is_palindrome("") is True
    assert solution.is_palindrome("a") is True
    assert solution.is_palindrome("madam") is True
    assert solution.is_palindrome("adam") is False
    assert solution.is_palindrome("tattarrattat") is True
