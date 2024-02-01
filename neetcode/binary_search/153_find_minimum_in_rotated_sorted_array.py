def find_min(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        middle = (l + r) // 2
        if nums[l] < nums[middle] < nums[r]:
            r = middle - 1
        elif nums[l] < nums[middle] and nums[middle] > nums[r]:
            l = middle + 1
        elif nums[l] > nums[middle] and nums[middle] < nums[r]:
            r = middle
        else:
            return min(nums[l], nums[r])

    return nums[l]


if __name__ == '__main__':
    print(find_min([123]))
    print(find_min([123]))
    print(find_min([123, 23]))
    print(find_min([3, 1, 2]))
    print(find_min([4, 7, 2]))
    print(find_min([3, 4, 5, 1, 2]))
    print(find_min([4, 5, 6, 7, 0, 1, 2]))
    print(find_min([11, 13, 15, 17]))
