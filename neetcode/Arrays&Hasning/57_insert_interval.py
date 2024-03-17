def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result = []
    start, end = new_interval

    i = 0
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append([start, end])

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result


if __name__ == '__main__':
    print(insert([[1, 3], [6, 9]], [2, 5]))
