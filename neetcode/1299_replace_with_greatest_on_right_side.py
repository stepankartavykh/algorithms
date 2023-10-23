import collections
from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    res = collections.deque([-1])
    greatest = -1
    for index in range(len(arr) - 1, 0, -1):
        if arr[index] > greatest:
            greatest = arr[index]
        res.appendleft(greatest)
    return list(res)


if __name__ == '__main__':
    print(replace_elements([17, 18, 5, 4, 6, 1]))
    print(replace_elements([400]))
