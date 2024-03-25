from collections import defaultdict


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    # TODO - resolve is required!
    already_connected = defaultdict(set)
    visited = defaultdict(bool)

    def is_already_connected(first, second):
        if first == second:
            return True
        for x_adjacent in already_connected[first]:
            if not visited[x_adjacent]:
                visited[x_adjacent] = True
                if is_already_connected(x_adjacent, second):
                    return True
        return False

    for edge in edges:
        x, y = edge[0], edge[1]
        if is_already_connected(x, y):
            return edge
        already_connected[x].add(y)
        already_connected[y].add(x)


if __name__ == '__main__':
    print(findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
    # print(findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
