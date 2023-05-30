"""
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character / number.
"""


from typing import List, cast


class Solution:
    def reverse_string(self, s: List[str | int]) -> None:
        """
        Do not return anything, modify s in-place instead.

        TC: O(n)
        SC: O(1)
        """
        for index in range(len(s) // 2):
            reverse_index = -(index + 1)
            s[index], s[reverse_index] = s[reverse_index], s[index]

    def reverse_string_recursive(self, s: List[str | int], start=0, end=None) -> None:
        """
        Do not return anything, modify s in-place instead.

        TC: O(n)
        SC: O(1)
        """
        if end is None:
            end = len(s) - 1

        if end <= start:
            return

        s[start], s[end] = s[end], s[start]
        self.reverse_string_recursive(s, start + 1, end - 1)


if __name__ == "__main__":
    solution = Solution()

    s1 = []
    solution.reverse_string(s1)
    assert s1 == []

    s2 = ["a", "b", "c", "d"]
    solution.reverse_string(cast(List[str | int], s2))
    assert s2 == ["d", "c", "b", "a"]

    s3 = ["h", "e", "l", "l", "o"]
    solution.reverse_string(cast(List[str | int], s3))
    assert s3 == ["o", "l", "l", "e", "h"]

    s4 = ["x"]
    solution.reverse_string(cast(List[str | int], s4))
    assert s4 == ["x"]

    s5 = ["a", "a", "a", "a"]
    solution.reverse_string(cast(List[str | int], s5))
    assert s5 == ["a", "a", "a", "a"]

    s6 = ["!", "@", "#", "$", "%"]
    solution.reverse_string(cast(List[str | int], s6))
    assert s6 == ["%", "$", "#", "@", "!"]

    s7 = [1, 2, 3, 4, 5]
    solution.reverse_string(cast(List[str | int], s7))
    assert s7 == [5, 4, 3, 2, 1]

    s8 = ["A", "b", "C", "d", "E"]
    solution.reverse_string(cast(List[str | int], s8))
    assert s8 == ["E", "d", "C", "b", "A"]

    s9 = [" ", "\t", "\n"]
    solution.reverse_string(cast(List[str | int], s9))
    assert s9 == ["\n", "\t", " "]

    s10 = ["1", "a", "@", "Z", "#"]
    solution.reverse_string(cast(List[str | int], s10))
    assert s10 == ["#", "Z", "@", "a", "1"]
