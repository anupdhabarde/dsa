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

    def merge_sort(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """

        def combine_sorted_lists(
            left_list: list[int], right_list: list[int]
        ) -> list[int]:
            """ """
            combined_list = []
            left_pointer = right_pointer = 0
            left_list_length = len(left_list)
            right_list_length = len(right_list)

            while left_pointer < left_list_length and right_pointer < right_list_length:
                if left_list[left_pointer] < right_list[right_pointer]:
                    combined_list.append(left_list[left_pointer])
                    left_pointer += 1
                else:
                    combined_list.append(right_list[right_pointer])
                    right_pointer += 1

            return combined_list + left_list[left_pointer:] + right_list[right_pointer:]

        nums_length = len(nums)

        if nums_length <= 1:
            return nums

        center = nums_length // 2

        return combine_sorted_lists(
            self.merge_sort(nums[:center]), self.merge_sort(nums[center:])
        )


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

    assert solution.merge_sort([10, 2, 4, 1, 8, 5, 6]) == [1, 2, 4, 5, 6, 8, 10]
    assert solution.merge_sort([]) == []
    assert solution.merge_sort([1]) == [1]
    assert solution.merge_sort([2, 1]) == [1, 2]
    assert solution.merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [
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
