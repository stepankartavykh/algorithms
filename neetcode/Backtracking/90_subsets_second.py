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


def subsets(nums: list[int]) -> list[list[int]]:
    # TODO is there a second way to implement this?
    result = []
    nums.sort()

    def backtrack(index, current_subset):
        if index == len(nums):
            result.append(current_subset.copy())
            return

        current_subset.append(nums[index])
        backtrack(index + 1, current_subset)
        current_subset.pop()
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1

        backtrack(index + 1, current_subset)

    backtrack(0, [])

    return result


if __name__ == '__main__':
    inputs = [
        [1, 2, 2],
        [0],
    ]
    for input_ in inputs:
        print(subsets_with_dup(input_))
        print(subsets(input_))
