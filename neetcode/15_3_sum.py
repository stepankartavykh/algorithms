from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for index, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target - num], index]
        hash_map[num] = index


def three_sum(nums: List[int]):
    triplets = []
    nums.sort()
    for index, num in enumerate(nums):
        if index > 0 and num == nums[index - 1]:
            continue

        left, right = index + 1, len(nums) - 1
        while left < right:
            sum_ = num + nums[left] + nums[right]
            if sum_ > 0:
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                triplets.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return triplets


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))
