from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    count_zeros = 0
    index = 0
    while index < len(nums):
        if nums[index] == 0:
            nums.pop(index)
            count_zeros += 1
            index -= 1
        index += 1
    nums.extend([0] * count_zeros)


def move_zeroes_second(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    for right in range(len(nums)):
        if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    move_zeroes_second(nums)
    print(nums)
    nums = [0]
    move_zeroes_second(nums)
    print(nums)
