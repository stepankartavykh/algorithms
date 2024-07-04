def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    seen = [False] * (n + 1)
    for num in nums:
        if 0 < num <= n:
            seen[num] = True
    for i in range(1, n + 1):
        if not seen[i]:
            return i
    return n + 1


def first_missing_positive_const_space_complexity(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        correct_index = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


def third_approach(nums: list[int]) -> int:
    nums = set(nums)
    x = 1
    while x in nums:
        x += 1
    return x


approaches = [
    first_missing_positive,
    first_missing_positive_const_space_complexity,
    third_approach,
]


def print_result(func, data):
    print(f"{func.__name__}({data}):", func(data))


if __name__ == '__main__':
    print("f([1, 2, 0]):", first_missing_positive_const_space_complexity([1, 2, 0]) == 3)
    print("f([2]):", first_missing_positive_const_space_complexity([2]) == 1)
    print("f([3, 4, -1, 1]):", first_missing_positive_const_space_complexity([3, 4, -1, 1]) == 2)
    print("f([7, 8, 9, 11, 12]):", first_missing_positive_const_space_complexity([7, 8, 9, 11, 12]) == 1)
    print("f([0, 2, 2, 1, 1]):", first_missing_positive_const_space_complexity([0, 2, 2, 1, 1]) == 3)
    print_result(third_approach, [1, 2, 3])