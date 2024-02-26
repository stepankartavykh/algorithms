def numberOfBST(n):
    # TODO Resolve this!
    nodes_counters = [0] * (n + 1)

    nodes_counters[0], nodes_counters[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(1, i + 1):
            nodes_counters[i] = nodes_counters[i] + (nodes_counters[i - j] * nodes_counters[j - 1])
    return nodes_counters[n]


if __name__ == "__main__":
    print(numberOfBST(1))
    print(numberOfBST(2))
    print(numberOfBST(3))
