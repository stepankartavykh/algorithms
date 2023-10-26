from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        position = (left + right) // 2
        if target > nums[position]:
            left = position + 1
        elif target < nums[position]:
            right = position - 1
        else:
            return position
    return -1


if __name__ == '__main__':
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4)
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=-1) == 0)
    print(search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1)
    print(search(nums=[0], target=0) == 0)
    print(search(nums=[0, 1], target=1) == 1)
    print(search(nums=[-1, 0, 5], target=5) == 2)
