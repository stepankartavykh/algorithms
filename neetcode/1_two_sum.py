from typing import List


def test_leet_code_cases():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], '1'
    assert two_sum([3, 2, 4], 6) == [1, 2], '2'
    assert two_sum([3, 3], 6) == [0, 1], '3'
    print('all tests passed!')


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_second_variant(nums: List[int], target: int) -> List[int]:
    pass


if __name__ == '__main__':
    test_leet_code_cases()
