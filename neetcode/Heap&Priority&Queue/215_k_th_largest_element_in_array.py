import heapq


def find_k_th_largest(nums: list[int], k: int) -> int:
    # TODO make QuickSelect algorithm.
    new_nums = [-n for n in nums]
    heapq.heapify(new_nums)
    for i in range(k - 1):
        heapq.heappop(new_nums)
    return -new_nums[0]


if __name__ == '__main__':
    print(find_k_th_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_k_th_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
