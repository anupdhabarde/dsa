"""
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.


Example 1:

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:

    - 1 <= nums.length <= 104
    - -104 < nums[i], target < 104
    - All the integers in nums are unique.
    - nums is sorted in ascending order.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """"""
        lower_bound = 0
        upper_bound = len(nums) - 1
        while lower_bound <= upper_bound:
            center = (lower_bound + upper_bound) // 2

            if nums[center] == target:
                return center

            if target > nums[center]:
                lower_bound = center + 1
            else:
                upper_bound = center - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    index = solution.search([-1, 0, 3, 5, 9, 12], 12)
    print(index)
