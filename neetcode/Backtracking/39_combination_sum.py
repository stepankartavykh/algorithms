def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(i: int, cur: list[int], total: int) -> None:
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


def combination_sum_with_sorting(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()

    result = []

    def backtrack(remaining_target: int, current_combination: list[int], start_index: int) -> None:
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
        ([2, 3, 5], 8),
    ]
    for input_ in inputs:
        print(combination_sum_with_sorting(input_[0], input_[1]))
