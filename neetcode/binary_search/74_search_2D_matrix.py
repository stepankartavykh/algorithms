from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    left, right = 0, len(matrix) - 1

    while left <= right:
        position = (left + right) // 2
        if target > matrix[position][0]:
            left = position + 1
        elif target < matrix[position][0]:
            right = position - 1
        else:
            return True

    if left > right:
        row = right
    else:
        row = left
    left, right = 0, len(matrix[0]) - 1

    while left <= right:
        position = (left + right) // 2
        if target > matrix[row][position]:
            left = position + 1
        elif target < matrix[row][position]:
            right = position - 1
        else:
            return True
    return False


if __name__ == '__main__':
    print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) is True)
    print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=0) is False)
    print(search_matrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=8) is False)
    print(search_matrix(matrix=[[0, 1], [2, 3]], target=4) is False)
    print(search_matrix(matrix=[[0, 1], [2, 3]], target=1) is True)
    print(search_matrix(matrix=[[0, 1], [2, 3]], target=3) is True)
