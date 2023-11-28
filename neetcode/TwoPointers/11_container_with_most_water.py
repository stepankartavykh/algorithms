from typing import List


def max_area(height: List[int]) -> int:

    left, right = 0, len(height) - 1
    max_amount = 0
    while left < right:

        amount = (right - left) * min(height[left], height[right])
        max_amount = max(amount, max_amount)
        if height[left] <= height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1

    return max_amount


if __name__ == '__main__':
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(max_area([7, 8, 6, 2, 5, 4, 8, 3, 7]))
