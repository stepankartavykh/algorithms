from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution_function([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print('all tests passed!')


def product_of_array_except_self(nums: List[int]) -> List[int]:
    total_product = 1
    zeros = []
    for position, num in enumerate(nums):
        if not num:
            zeros.append(position)
        else:
            total_product *= num
        if len(zeros) == 2:
            return [0] * len(nums)
    length = len(zeros)
    if length >= 2:
        return [0] * len(nums)
    elif length == 1:
        arr = [0] * len(nums)
        arr[zeros[0]] = total_product
        return arr
    else:
        return [int(total_product / element) for element in nums]


if __name__ == '__main__':
    print(product_of_array_except_self([1, 2, 3, 4]))
    print(product_of_array_except_self([-1, 1, 0, -3, 3]))
    test_leet_code_cases(product_of_array_except_self)
