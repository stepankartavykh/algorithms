from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    # TODO time complexity - O(n * 2^n)?
    result = []
    subset = []

    def find_solutions(index):
        if index >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        find_solutions(index + 1)
        subset.pop()
        find_solutions(index + 1)

    find_solutions(0)

    return result


if __name__ == '__main__':
    inputs = [
        [0],
        [2, 3],
        [1, 2, 3],
    ]
    for input_ in inputs:
        print(subsets(input_))
