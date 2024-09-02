import heapq


def max_product(nums: list[int]) -> int:
    nums = [-n for n in nums]
    heapq.heapify(nums)
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    return (-first - 1) * (-second - 1)


if __name__ == '__main__':
    print(max_product([3, 4, 5, 2]))
