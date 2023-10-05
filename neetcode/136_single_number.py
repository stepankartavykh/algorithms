import functools
from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([2, 2, 1]) == 1
    assert solution_function([4, 1, 2, 1, 2]) == 4
    assert solution_function([1]) == 1
    print('all tests passed!')


def single_number(nums: List[int]) -> int:
    return functools.reduce(lambda first, second: first ^ second, nums)


if __name__ == '__main__':
    test_leet_code_cases(single_number)
