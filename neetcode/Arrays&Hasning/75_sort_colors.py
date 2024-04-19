def sort_colors(nums: list[int]) -> list[int]:
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid +=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


if __name__ == '__main__':
    print(sort_colors([0, 2, 1, 1, 2, 0, 1]))
