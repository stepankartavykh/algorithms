from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    subset = []

    def find_solutions(index):
        if index >= len(candidates):
            if sum(subset) == target:
                result.append(subset.copy())
            return
        current_val = candidates[index]
        current_subset = subset.copy()

        while sum(subset) < target:
            subset.append(current_val)
            find_solutions(index + 1)

        find_solutions(index + 1)

        subset.pop()

        find_solutions(index + 1)


    find_solutions(0)

    return result


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()

    result = []

    def backtrack(remaining_target, current_combination, start_index):
        if remaining_target == 0:
            result.append(list(current_combination))
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > remaining_target:
                break

            current_combination.append(candidates[i])

            backtrack(remaining_target - candidates[i], current_combination, i)

            current_combination.pop()

    backtrack(target, [], 0)

    return result


if __name__ == '__main__':
    inputs = [
        ([2, 3, 6, 7], 7),
        # ([2, 3, 5], 8),
    ]
    for input_ in inputs:
        # print(combination_sum(input_[0], input_[1]))
        print(combinationSum(input_[0], input_[1]))
