from collections import defaultdict
import heapq


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def min_cost_to_connect_points(points):
    n = len(points)
    min_cost = 0
    visited = set()
    min_heap = [(0, 0)]

    while len(visited) < n:
        cost, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        min_cost += cost

        for i in range(n):
            if i != node and i not in visited:
                heapq.heappush(min_heap, (manhattan_distance(points[node], points[i]), i))

    return min_cost


def min_cost_to_connect_all_points(points: list[list[int]]) -> int:
    edge_to_distance = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            edge = (points[i][0], points[i][1], points[j][0], points[j][1])
            distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edge_to_distance.append((edge, distance))

    edge_to_distance.sort(key=lambda element: element[1])

    def connected(first: tuple[int, int], second: tuple[int, int], adj: dict) -> bool:
        return True

    print(edge_to_distance)
    adj_list = defaultdict(set)
    for edge in edge_to_distance:
        one_p = edge[0][0], edge[0][1]
        second_p = edge[0][2], edge[0][3]
        dist = edge[1]
        if one_p in adj_list:
            while True:
                neighbours = adj_list[one_p]
                for neighbour in neighbours:
                    pass

    print()
    for k, v in adj_list.items():
        print(k, v)
    edges_limit = len(points)


if __name__ == '__main__':
    print(min_cost_to_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
    # print(min_cost_to_connect_points([[3, 12], [-2, 5], [-4, 1]]))
