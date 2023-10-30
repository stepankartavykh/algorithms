from typing import List


def minimum_difference(nums: List[int], k: int) -> int:
    nums.sort()
    left, right = 0, k - 1
    difference = float('inf')
    while right < len(nums):
        difference = min(difference, nums[right] - nums[left])
        left, right = left + 1, right + 1
    return difference


if __name__ == '__main__':
    print(minimum_difference(nums=[90], k=1))
    print(minimum_difference(nums=[9, 4, 1, 7], k=2))
    print(minimum_difference(nums=[9, 4, 1, 7, 11, 10], k=2))
