def is_monotonic(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    first, second = 0, 1
    while second < len(nums) and nums[first] == nums[second]:
        first += 1
        second += 1
    if second >= len(nums):
        return True
    increasing = True
    if nums[first] > nums[second]:
        increasing = False
    while second < len(nums):
        if increasing:
            if nums[first] > nums[second]:
                return False
        else:
            if nums[first] < nums[second]:
                return False
        first += 1
        second += 1
    return True


if __name__ == '__main__':
    print(is_monotonic([1, 1, 1]))
