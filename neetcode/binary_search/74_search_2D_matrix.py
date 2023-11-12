from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, len(matrix) - 1

    while left < right:
        position = (left + right) // 2
        if target > matrix[position][0]:
            left = position + 1
        elif target < matrix[position][0]:
            right = position - 1
        else:
            return True

    row = left
    left, right = 0, len(matrix[0])

    while left < right:
        position = (left + right) // 2
        if target > matrix[row][position]:
            left = position + 1
        elif target < matrix[row][position]:
            right = position - 1
        else:
            return True

    print(left, right)


if __name__ == '__main__':
    print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) is True)
