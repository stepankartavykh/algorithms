from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    result = []
    while left < right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            result.append(nums[left] * nums[left])
            left += 1
        else:
            result.append(nums[right] * nums[right])
            right -= 1

    return result[::-1]  # TODO is it better?


if __name__ == '__main__':
    inputs = [
        [-1],
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [0, 1, 2],
        [-1, 0, 1, 2],
        [-1, 1, 2],
        [-2]
    ]
    for input_ in inputs:
        print(sorted_squares(input_))
