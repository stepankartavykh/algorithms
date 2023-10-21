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


if __name__ == '__main__':
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    print(remove_element(a, 2))
    print(a)
