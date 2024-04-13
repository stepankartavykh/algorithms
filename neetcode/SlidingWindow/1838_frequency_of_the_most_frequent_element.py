from typing import List


def max_frequency(nums: List[int], k: int) -> int:
    nums.sort()
    l, r = 0, 0
    max_freq = 0
    total = 0
    while r < len(nums):
        total += nums[r]
        # condition on "invalid" window
        # 1) nums[r] * (r - l + 1) - possible sum of elements in window - max element of window * length of window
        # 2) total (real sum of current window) + count of 1 that we can add to elements in window
        # if 1) > 2) so that means we need to subtract window to get maximum possible count of elements
        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 1
        max_freq = max(max_freq, r - l + 1)
        r += 1
    return max_freq


if __name__ == '__main__':
    inputs = [
        ([1, 2, 4], 5),
        ([1, 4, 8, 13], 5),
        ([1, 1, 1, 3], 1),
        ([9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990,
          9994, 9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959,
          9957, 9907, 9913, 9916, 9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925,
          9923, 9904, 9928, 9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917,
          9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966], 3056),
    ]
    for input_ in inputs:
        print(max_frequency(input_[0], input_[1]))
