from collections import defaultdict


def dest_city(paths: list[list[str]]) -> str:
    adj = defaultdict(list)
    for city_from, city_to in paths:
        adj[city_from].append(city_to)
    inp = adj[paths[0][0]][0]
    while True:
        next_cities = adj[inp]
        inp = next_cities[0]
        if inp not in adj:
            return inp


if __name__ == '__main__':
    print(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    print(dest_city([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(dest_city([["A", "Z"]]))
