def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    diff = [g - c for g, c in zip(gas, cost)]
    if sum(diff) < 0:
        return -1
    for pos in range(len(diff)):
        if diff[pos] > 0:
            start_pos = pos
            current_gas = 0
            for i in range(start_pos, len(diff) + start_pos):
                if i >= len(diff):
                    current_gas += diff[i - len(diff)]
                else:
                    current_gas += diff[i]
                if current_gas < 0:
                    break
            else:
                return pos
        elif diff[pos] == 0:
            if len(diff) == 1:
                return 0


def trav(arr: list, start: int):
    for i in range(start, len(arr) + start):
        if i >= len(arr):
            print(arr[i - len(arr)])
        else:
            print(arr[i])


if __name__ == '__main__':
    # trav([1, 2, 3, 4, 5, 6], 2)
    print(canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    print(canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]))
    print(canCompleteCircuit(gas=[2], cost=[2]))
