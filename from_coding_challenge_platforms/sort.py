class Solution:
    def bubble_sort(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums) - 1):
            is_swapped = False
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    is_swapped = True

            if not is_swapped:
                break

        return nums

    def selection_sort(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums) - 1):
            smallest_num_index = i

            for j in range(i + 1, len(nums)):
                if nums[j] < nums[smallest_num_index]:
                    smallest_num_index = j

            if smallest_num_index != i:
                nums[i], nums[smallest_num_index] = nums[smallest_num_index], nums[i]

        return nums


if __name__ == "__main__":
    solution = Solution()
    assert solution.bubble_sort([10, 2, 4, 1, 8, 5, 6]) == [1, 2, 4, 5, 6, 8, 10]
    assert solution.bubble_sort([]) == []
    assert solution.bubble_sort([1]) == [1]
    assert solution.bubble_sort([2, 1]) == [1, 2]
    assert solution.bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
    assert solution.selection_sort([10, 2, 4, 1, 8, 5, 6]) == [1, 2, 4, 5, 6, 8, 10]
    assert solution.selection_sort([]) == []
    assert solution.selection_sort([1]) == [1]
    assert solution.selection_sort([2, 1]) == [1, 2]
    assert solution.selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ]
