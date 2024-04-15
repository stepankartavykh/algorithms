from collections import defaultdict


def min_time(n: int, edges: list[list[int]], has_apple: list[bool]) -> int:
    adj_list = defaultdict(set)
    for one, two in edges:
        adj_list[one].add(two)
        adj_list[two].add(one)

    def dfs(node, parent):
        time = 0

        for child in adj_list[node]:
            if child == parent:
                continue
            child_time = dfs(child, node)

            if child_time or has_apple[child]:
                time += 2 + child_time
        return time

    return dfs(0, -1)


if __name__ == '__main__':
    print(min_time(n=7,
                   edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                   has_apple=[False, False, True, False, True, True, False]))
