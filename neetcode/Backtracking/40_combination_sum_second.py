def combination_sum_second(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    current_subset = []

    candidates.sort()

    def backtrack(i_start, i_current):
        if i_start < len(candidates) and i_current < len(candidates):
            if sum(current_subset) + candidates[i_current] == target:
                current_subset.append(candidates[i_current])
                result.append(current_subset.copy())
                current_subset.clear()
                backtrack(i_start + 1, i_start + 1)
                return

            current_subset.append(candidates[i_start])
            for cur_index in range(i_current + 1, len(candidates)):
                current_subset.append(candidates[cur_index])
                backtrack(i_start, cur_index)
                if current_subset:
                    current_subset.pop()

            if current_subset:
                current_subset.pop()

            if not current_subset:
                backtrack(i_start + 1, i_start + 1)

    backtrack(0, 0)

    return result


if __name__ == '__main__':
    inputs = [
        [[5], 5],
        [[2, 5, 2, 1, 2], 5],
        [[10, 1, 2, 7, 6, 1, 5], 8],
    ]
    for input_ in inputs:
        print(combination_sum_second(input_[0], input_[1]))
