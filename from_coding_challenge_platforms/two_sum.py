"""
https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]


Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]


Constraints:

    - 2 <= nums.length <= 104
    - -109 <= nums[i] <= 109
    - -109 <= target <= 109
    - Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""


class Solution:
    def brute_force(self, nums: list[int], target: int) -> list[int]:
        """
        Loop through each element x and find if there is another value that equals to target-x.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        num_length = len(nums)

        for index, num in enumerate(nums):
            if index == num_length - 1:
                break

            for j in range(index + 1, num_length):
                if num + nums[j] == target:
                    return [index, j]

        return [-1, -1]

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        Intuition:

        To improve our runtime complexity, we need a more efficient way to check if the complement exists in the array.
        If the complement exists, we need to get its index.
        What is the best way to maintain a mapping of each element in the array to its index? A hash table.

        We can reduce the lookup time from O(n) to O(1) by trading space for speed.
        A hash table is well suited for this purpose because it supports fast lookup in near constant time.
        I say "near" because if a collision occurred, a lookup could degenerate to O(n) time.
        However, lookup in a hash table should be amortized O(1) time as long as the hash function was chosen carefully.

        Algorithm:

        While we are iterating and inserting elements into the hash table, we also look back to check if current element's
        complement already exists in the hash table.
        If it exists, we have found a solution and return the indices immediately.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        hash_map = {}

        for index, num in enumerate(nums):
            delta = target - num

            if delta in hash_map:
                return [hash_map[delta], index]

            hash_map[num] = index

        return [-1, -1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.brute_force([2, 7, 11, 15], 9) == [0, 1]
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
