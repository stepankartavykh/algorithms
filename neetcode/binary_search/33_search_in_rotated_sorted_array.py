from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m
# TODO remove this crutch!
        elif nums[r] == target:
            return r
        elif nums[l] <= target <= nums[m] or (nums[l] >= nums[m] and not nums[m] <= target <= nums[r]):
            r = m - 1
        elif nums[m] <= target <= nums[r] or (nums[m] >= nums[r] and not nums[l] <= target <= nums[m]):
            l = m + 1
        elif not nums[l] <= target <= nums[m] and not nums[m] <= target <= nums[r]:
            return -1
# TODO return -1 two times? Can we do better?
    return -1


if __name__ == '__main__':
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(search(nums=[3, 1], target=1))
    print(search(nums=[3, 1], target=3))
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=6))
    print(search(nums=[7, 0, 1, 2], target=5))
    print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(search(nums=[1], target=0))
