from typing import List
import heapq


def last_stone_weight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if first != second:
            heapq.heappush(stones, -abs(first - second))
    if stones:
        return -stones.pop()
    else:
        return 0


if __name__ == '__main__':
    input_structures = [
        [2, 7, 4, 1, 8, 1],
        [1],
        [1, 2, 3, 1, 5, 7, 10],
        [1, 2, 3],
        [1, 1000],
        [4, 3, 4, 3, 2],
        [2, 3, 4, 3, 4, 4, 4]
    ]
    for struct in input_structures:
        print(last_stone_weight(struct))
