def debug(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j:
                print(i, j, nums[i] & nums[j] == 0)


def longest_nice_subarray(nums: list[int]) -> int:
    l, r = 0, 1
    res = 1

    while r < len(nums):
        new_number = nums[r]
        for k in range(l, r):
            if nums[k] & new_number != 0:
                l += 1
                break
        else:
            r += 1
            res = max(res, r - l + 1)

    return res


if __name__ == '__main__':
    print([1, 3, 8, 48, 10], '-', longest_nice_subarray([1, 3, 8, 48, 10]) == 3)
    print([1], '-', longest_nice_subarray([1]) == 1)
    print([1, 2], '-', longest_nice_subarray([1, 2]) == 2)
    print([1, 2, 3], '-', longest_nice_subarray([1, 2, 3]) == 2)
    # print('last', longest_nice_subarray(
    #     [84139415, 693324769, 614626365, 497710833, 615598711, 264, 65552, 50331652, 1, 1048576, 16384, 544, 270532608,
    #      151813349, 221976871, 678178917, 845710321, 751376227, 331656525, 739558112, 267703680]) == 8)
