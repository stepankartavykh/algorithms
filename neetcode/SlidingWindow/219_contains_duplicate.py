from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    unique = set()
    left = 0

    for index in range(len(nums)):
        if index - left > k:
            unique.remove(nums[left])
            left += 1
        if nums[index] in unique:
            return True
        unique.add(nums[index])
    return False


if __name__ == '__main__':
    print(contains_nearby_duplicate([2, 2], 3) is True)
    print(contains_nearby_duplicate([1, 2, 3, 1], 3) is True)
    print(contains_nearby_duplicate([1, 0, 1, 1], 1) is True)
    print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False)
