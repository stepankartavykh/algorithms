from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution_function([-1, 1, 0, -3, 3], 1) == [0, 0, 9, 0, 0]
    print('all tests passed!')


def product_of_array_except_self(nums: List[int]) -> List[int]:
    total_product = 1
    zeros = set()
    for position, num in enumerate(nums):
        total_product *= num
        if not num:
            zeros.add(position)

        if len(zeros) == 2:
            return [0] * len(nums)
    answer = []
    for num in nums:
        answer_element = 1


if __name__ == '__main__':
    print(product_of_array_except_self([1, 2, 3, 4]))
    print(product_of_array_except_self([-1, 1, 0, -3, 3]))
    test_leet_code_cases(product_of_array_except_self)
