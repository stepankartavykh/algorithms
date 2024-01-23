from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    rows, columns = len(grid), len(grid[0])
    perimeter = 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                if column == 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                if row == 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                if column == columns - 1 or grid[row][column + 1] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter


if __name__ == '__main__':
    print(island_perimeter(
        grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    ))
