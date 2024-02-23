def max_area_of_island(grid: list[list[int]]) -> int:
    max_area = 0
    max_rows, max_columns = len(grid), len(grid[0])
    visited_lands = set()

    def calc_area(r, c):
        if r < 0 or r >= max_rows or c < 0 or c >= max_columns or not grid[r][c] or (r, c) in visited_lands:
            return 0
        visited_lands.add((r, c))
        return 1 + calc_area(r + 1, c) + calc_area(r - 1, c) + calc_area(r, c + 1) + calc_area(r, c - 1)

    for row in range(max_rows):
        for column in range(max_columns):
            if grid[row][column]:
                max_area = max(max_area, calc_area(row, column))

    return max_area


if __name__ == '__main__':
    print(max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]))
    print(max_area_of_island([[0, 0, 1, 0],
                              [0, 0, 1, 0],
                              [0, 0, 1, 1],
                              ]))
    print(max_area_of_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
