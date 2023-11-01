from typing import List


def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        position = (left + right) // 2
        if target > nums[position]:
            left = position + 1
        elif target < nums[position]:
            right = position - 1
        else:
            return position
    return left


if __name__ == '__main__':
    print(search_insert(nums=[1, 3, 5, 6], target=5) == 2)
    print(search_insert(nums=[1, 3, 5, 6], target=2) == 1)
    print(search_insert(nums=[1, 3, 5, 6], target=7) == 4)
    print(search_insert(nums=[1], target=1) == 0)
    print(search_insert(nums=[1], target=2) == 1)
    print(search_insert(nums=[1], target=-1) == 0)
    print(search_insert(nums=[1, 3], target=2) == 1)
    print(search_insert(nums=[1, 3], target=-3) == 0)
