def find_max_length(nums: list[int]) -> int:
    res = 0
    diff = 0
    diff_index = {}

    for index, num in enumerate(nums):
        if num:
            diff += 1
        else:
            diff -= 1

        if diff == 0:
            res = max(res, index + 1)
        else:
            if diff not in diff_index:
                diff_index[diff] = index
            else:
                res = max(res, index - diff_index[diff])

    return res


if __name__ == '__main__':
    print(find_max_length([1, 1, 0, 1, 1, 1, 0, 0, 1]))
