from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # TODO must be O(n). n^2 right now!
        d = {}
        for i in range(len(nums)):
            d[i] = sum(nums[:i+1])
        self.sums = d

    def sum_range(self, left: int, right: int) -> int:
        # TODO delete if statement by rewriting constructor
        if left > 0:
            return self.sums[right] - self.sums[left - 1]
        else:
            return self.sums[right]


if __name__ == '__main__':
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print(arr.sum_range(0, 2), 1)
    print(arr.sum_range(2, 5), -1)
    print(arr.sum_range(0, 5), -3)
