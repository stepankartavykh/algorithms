from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    input_structures = [
        ([[3, [4, 5, 8, 2]], [[3], [5], [10], [9], [4]]]),
        ([[2, [0]], [[-1], [1], [-2], [-4], [3]]]),
    ]
    for struct in input_structures:
        kth_struct = KthLargest(struct[0][0], struct[0][1])
        for elem in struct[1]:
            print(kth_struct.add(elem[0]), end=' ')
        print()
