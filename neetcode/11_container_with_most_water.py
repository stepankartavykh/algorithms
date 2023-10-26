from typing import List


def max_area(height: List[int]) -> int:

    left, right = 0, len(height) - 1
    max_amount = 0
    while left < right:

        amount = (right - left) * min(height[left], height[right])
        if amount > max_amount:
            max_amount = amount
        left += 1
        right -= 1

    return max_amount


if __name__ == '__main__':
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
