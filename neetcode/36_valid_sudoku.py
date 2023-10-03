from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution_function([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print('all tests passed!')


def is_valid_sudoku(board: List[List[str]]) -> bool:
    for y, row in enumerate(board):
        row_set = set()
        for x, current_cell in enumerate(row):
            column_set = set()
            if current_cell != '.':
                if current_cell in row_set:
                    return False
                else:
                    row_set.add(current_cell)
            print(current_cell, end=' ')
        print()


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
