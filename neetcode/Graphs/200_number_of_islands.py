from collections import deque
from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    # TODO MUST be resolved!!!
    islands = 0
    visited = set()

    rows, columns = len(grid), len(grid[0])

    def visit_whole_land_of_island(r, c):
        visited.add((r, c))
        cells_of_island = deque()
        cells_of_island.append((r, c))

        while cells_of_island:
            row, column = cells_of_island.popleft()
            deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for delta_row, delta_column in deltas:
                possible_row, possible_column = row + delta_row, column + delta_column
                if possible_row in range(rows) and possible_column in range(columns) and grid[possible_row][possible_column] == '1' and (possible_row, possible_column) not in visited:
                    visited.add((possible_row, possible_column))
                    cells_of_island.append((possible_row, possible_column))

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '1' and (row, column) not in visited:
                visit_whole_land_of_island(row, column)
                islands += 1

    return islands


if __name__ == '__main__':
    grids = [
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ],
    ]
    for grid_ in grids:
        print(number_of_islands(grid_))
