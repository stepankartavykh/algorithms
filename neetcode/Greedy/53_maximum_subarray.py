def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    total = 0

    for num in nums:
        total += num
        max_sum = max(max_sum, total)
        if total < 0:
            total = 0

    return max_sum


if __name__ == '__main__':
    print(maxSubArray([-2, -11]))
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
