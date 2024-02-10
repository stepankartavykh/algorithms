def permute(nums: list[int]) -> list[list[int]]:
    # TODO Resolve this later!
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for _ in range(len(nums)):
        first_element_left = nums.pop(0)

        permutations_of_nums_without_first_element = permute(nums)

        for permutation in permutations_of_nums_without_first_element:
            permutation.append(first_element_left)
        result.extend(permutations_of_nums_without_first_element)

        nums.append(first_element_left)

    return result


if __name__ == '__main__':
    inputs = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]
    for input_ in inputs:
        print(permute(input_))
