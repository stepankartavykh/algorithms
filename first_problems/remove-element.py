from typing import List


def remove_element(nums: List[int], val: int) -> int:
    k = 0
    index = 0
    while index < len(nums):
        if nums[index] == val:
            nums.pop(index)
            index -= 1
            k += 1
        index += 1
    return k


def second_approach(nums: List[int], val: int) -> int:
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


if __name__ == '__main__':
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    print(second_approach(a, 2))
    print(a)
