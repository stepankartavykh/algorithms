from collections import OrderedDict, deque


def partition_labels(s: str) -> list[int]:
    letter_to_pos = {}
    for index, symbol in enumerate(s):
        if symbol in letter_to_pos:
            letter_to_pos[symbol][1] = index
        else:
            letter_to_pos[symbol] = [index, index]
    positions = OrderedDict(sorted(letter_to_pos.items(), key=lambda x: x[1][0])).values()
    positions = deque(positions)
    result = []
    while positions:
        first_start, first_end = positions.popleft()
        if positions:
            second_start, second_end = positions.popleft()
        else:
            result.append(first_end - first_start + 1)
            break
        if second_start > first_end:
            result.append(first_end - first_start + 1)
            positions.appendleft([second_start, second_end])
        else:
            period = [first_start, max(first_end, second_end)]
            positions.appendleft(period)

    return result


if __name__ == '__main__':
    print(partition_labels('ababcbacadefegdehijhklij'))