from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0]
        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num)

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


if __name__ == '__main__':
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print(arr.sum_range(0, 2), 1)
    print(arr.sum_range(2, 5), -1)
    print(arr.sum_range(0, 5), -3)
