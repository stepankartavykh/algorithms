def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # TODO Analyse how this solution works! Resolve later!

    res = []
    nums.sort()

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return

        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res


if __name__ == '__main__':
    inputs = [
        [1, 2, 2],
        [0],
    ]
    for input_ in inputs:
        print(subsets_with_dup(input_))
