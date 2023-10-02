from collections import defaultdict
from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert solution_function([1], 1) == [1]
    assert solution_function([1, 10, 2, 3, 10, 2, 4, 3, 3], 3) == [2, 3, 10]
    print('all tests passed!')


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    answer = defaultdict(int)
    for num in nums:
        answer[num] += 1
    answer = sorted(answer.items(), key=lambda element: element[1], reverse=True)
    return [elem[0] for elem in answer][:k]


if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent([1], 1))
    print(top_k_frequent([1, 10, 2, 3, 10, 2, 4, 3, 3], 3))
    # TODO make handy test function
    test_leet_code_cases(top_k_frequent)
