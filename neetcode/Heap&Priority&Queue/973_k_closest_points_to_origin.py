import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    # TODO (make your own heapify may be)
    distances = [
        [coords[0] * coords[0] + coords[1] * coords[1], index]
        for index, coords in enumerate(points)
    ]
    heapq.heapify(distances)
    closest_points = []
    for _ in range(k):
        _, index = heapq.heappop(distances)
        closest_points.append(points[index])
    return closest_points


if __name__ == '__main__':
    print(k_closest([[1, 3], [-2, 2]], 1))
    print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
