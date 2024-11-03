def merge(intervals: list[list[int]]) -> list[list[int]]:
    res = []
    intervals.sort(key=lambda elem: elem[0])
    for i in range(len(intervals)):
        last_elem = res.pop() if res else None
        if last_elem:
            if last_elem[0] <= intervals[i][0] <= last_elem[1]:
                if intervals[i][1] <= last_elem[1]:
                    res.append(last_elem)
                else:
                    res.append([last_elem[0], intervals[i][1]])
            else:
                res.append(last_elem)
                res.append(intervals[i])
        else:
            res.append(intervals[i])
    return res


def test_merge():
    assert merge([[1, 3], [1, 3]]) == [[1, 3]]
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[2,3]]) == [[1,4]]
