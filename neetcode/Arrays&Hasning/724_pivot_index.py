from typing import List


class Solution:
    @staticmethod
    def pivot_index(nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for index in range(len(nums)):
            right_sum = total_sum - nums[index] - left_sum
            if left_sum == right_sum:
                return index
            left_sum += nums[index]
        return -1


if __name__ == '__main__':
    inputs = [
        [1, 7, 3, 6, 5, 6],
        [1, 2, 3],
        [2, 1, -1],
        [1, 2],
        [-1, -1, 0, 1, 1, 0],
        [1],
    ]
    for input_ in inputs:
        print(Solution.pivot_index(input_))
