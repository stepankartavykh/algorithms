from collections import deque
from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            pass
        self.elements = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        self.elements.append(val)
        return sorted(self.elements, reverse=True)[self.k - 1]


def test_heap():
    heap = []

    heapq.heappush(heap, 5)
    heapq.heappush(heap, 2)
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 7)
    heapq.heappush(heap, 3)

    print("Heap:", heap)

    smallest = heapq.heappop(heap)
    print("Smallest element:", smallest)
    print("Heap after pop:", heap)

    n_smallest = heapq.nsmallest(3, heap)
    print("N smallest elements:", n_smallest)

    data = [8, 1, 6, 4, 9]
    heapq.heapify(data)
    print("Heapified data:", data)


if __name__ == '__main__':
    # kthLargest = KthLargest(3, [4, 5, 8, 2])
    # print(kthLargest.add(3))
    # print(kthLargest.add(5))
    # print(kthLargest.add(10))
    # print(kthLargest.add(9))
    # print(kthLargest.add(4))
    test_heap()