from collections import defaultdict
from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution_function([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print('all tests passed!')


def is_valid_sudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    sectors = defaultdict(set)
    for row in range(9):
        for column in range(9):
            if board[row][column] == '.':
                continue
            elif board[row][column] in rows[row] or board[row][column] in columns[column] or board[row][column] in sectors[3 * (row // 3) + column // 3]:
                return False
            else:
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                sectors[3 * (row // 3) + column // 3].add(board[row][column])
    return True


if __name__ == '__main__':
    print(is_valid_sudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
    print(is_valid_sudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
    # test_leet_code_cases(is_valid_sudoku)
