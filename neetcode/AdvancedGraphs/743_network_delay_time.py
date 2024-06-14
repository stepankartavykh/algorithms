from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj_list = defaultdict(set)
    for element in times:
        from_, to_, travel_time = element
        adj_list[from_].add((to_, travel_time))
    received = [False] * n

    while True:
        next_nodes = adj_list[k]
        times = [n[1] for n in next_nodes]
        break

    print(dict(adj_list))

    return 0


if __name__ == '__main__':
    network_delay_time(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
