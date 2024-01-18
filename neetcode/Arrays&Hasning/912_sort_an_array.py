from typing import List


def sort_array(nums: List[int]) -> List[int]:
    # TODO make analysis on memory usage and time complexity. COMPARE!
    if len(nums) < 2:
        return nums
    stage_element = nums[0]
    left = [elem for elem in nums[1:] if elem <= stage_element]
    right = [elem for elem in nums[1:] if elem > stage_element]

    return sort_array(left) + [stage_element] + sort_array(right)


def merge_sort(nums):
    # TODO make analysis on memory usage and time complexity. COMPARE!
    if len(nums) < 2:
        return nums
    if len(nums) == 2:
        return [min(nums), max(nums)]

    center_index = len(nums) // 2

    left_array = merge_sort(nums[:center_index])
    right_array = merge_sort(nums[center_index:])

    pointer, left_pointer, right_pointer = 0, 0, 0

    while pointer < len(nums):

        left_element = left_array[left_pointer] if left_pointer < len(left_array) else None
        right_element = right_array[right_pointer] if right_pointer < len(right_array) else None

        if left_element is not None and right_element is not None:
            if left_element <= right_element:
                nums[pointer] = left_element
                left_pointer += 1
            else:
                nums[pointer] = right_element
                right_pointer += 1
        elif left_element is None:
            nums[pointer] = right_element
            right_pointer += 1
        elif right_element is None:
            nums[pointer] = left_element
            left_pointer += 1

        pointer += 1

    return nums


if __name__ == '__main__':
    print(sort_array([5, 2, 3, 1]))
    print(sort_array([5, 1, 1, 2, 0, 0]))

    print(merge_sort([5, 2, 3, 1]))
    print(merge_sort([5, 1, 1, 2, 0, 0]))
    print(merge_sort([3, 1, 123]))
