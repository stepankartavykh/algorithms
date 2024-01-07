from typing import List


def single_non_duplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if ((middle < 1 or nums[middle] != nums[middle - 1]) and
                (middle + 1 == len(nums) or nums[middle] != nums[middle + 1])):
            return nums[middle]

        count_left_nums = middle - 1 if nums[middle] == nums[middle - 1] else middle
        if count_left_nums % 2 > 0:
            right = middle - 1
        else:
            left = middle + 1


if __name__ == '__main__':
    print(single_non_duplicate([1]))
    print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
