from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([100, 4, 200, 1, 3, 2]) == 4
    assert solution_function([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    print('all tests passed!')


def longest_consecutive(nums: List[int]) -> int:
    longest = 0
    num_set = set(nums)

    for n in num_set:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)
    return longest


if __name__ == '__main__':
    test_leet_code_cases(longest_consecutive)
