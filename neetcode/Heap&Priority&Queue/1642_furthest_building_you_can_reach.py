import heapq


def can_reach(heights: list[int], bricks: int, ladders: int) -> bool:
    sum_diffs = 0
    count_diffs = 0
    for i in range(len(heights) - 1):
        if heights[i + 1] > heights[i]:
            sum_diffs += heights[i + 1] - heights[i]
            count_diffs += 1
    if sum_diffs - bricks - ladders <= 0:
        return True
    if ladders >= count_diffs:
        return True
    return False


def furthest_building(heights: list[int], bricks: int, ladders: int) -> int:
    for i in range(len(heights) - 1, -1, -1):
        if can_reach(heights[:i+1], bricks, ladders):
            print(i, heights[:i+1])
            return i


def furthest_building_solution(heights: list[int], bricks: int, ladders: int) -> int:
    heap = []
    for i in range(len(heights) - 1):
        diff = heights[i + 1] - heights[i]
        if diff <= 0:
            continue
        bricks -= diff
        heapq.heappush(heap, -diff)
        if bricks < 0:
            bricks += -heapq.heappop(heap)
            ladders -= 1
        if ladders < 0:
            return i
    return len(heights) - 1


if __name__ == '__main__':
    print(furthest_building_solution([4, 2, 7, 6, 9, 14, 12], 5, 1))
    print(furthest_building_solution([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2))
    print(furthest_building_solution([14, 3, 19, 3], 17, 0))
