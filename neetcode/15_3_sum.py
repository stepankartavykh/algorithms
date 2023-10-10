from typing import List


def three_sum(nums: List[int]):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        while nums[left] + nums[right] > 0:
            right -= 1
        while nums[left] + nums[right] < 0:
            left += 1
        if nums[left] + nums[right] == 0:
            return [left + 1, right + 1]
