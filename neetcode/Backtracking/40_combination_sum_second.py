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


def combination_sum_not_my_solution(candidates: list[int], target: int) -> list[list[int]]:
    # TODO Resolve later

    # Sort array with numbers
    candidates.sort()

    result = []

    # Define backtracking function
    def backtrack(cur_subset, cur_position, cur_target):
        # If cur_target is zero - add cur_subset. By the way [] not include in results due to constraints.
        if cur_target == 0:
            result.append(cur_subset.copy())
            return
        # If sum of elements > target, then we pass negative value to backtracking function, so we need to end this
        # leave on this stage of decision tree.
        if target <= 0:
            return

        # TODO This place with previous = -1 requires analysis.
        previous = -1
        for i in range(cur_position, len(candidates)):
            # Comparison to avoid duplicates.
            if candidates[i] == previous:
                continue
            # Add value to subset to jump inside this path.
            cur_subset.append(candidates[i])
            backtrack(cur_subset, i + 1, cur_target - candidates[i])
            # TODO Why don't we call the function again after pop() from cur_subset?
            cur_subset.pop()
            # Store value we added to cur_subset.
            previous = candidates[i]

    backtrack([], 0, target)

    return result


if __name__ == '__main__':
    inputs = [
        [[5], 5],
        [[2, 5, 2, 1, 2], 5],
        [[10, 1, 2, 7, 6, 1, 5], 8],
    ]
    for input_ in inputs:
        print(combination_sum_not_my_solution(input_[0], input_[1]))
