import collections


def oranges_rotting(grid: list[list[int]]) -> int:
    # TODO (Resolve later)
    rows = len(grid)
    columns = len(grid[0])

    minutes = 0
    fresh = 0
    rotten_oranges = collections.deque()

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                rotten_oranges.append((r, c))

    displacements = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # very useful technique to make two conditions in while statement in case of bfs (in another cases too)
    while fresh and rotten_oranges:
        for _ in range(len(rotten_oranges)):
            r, c = rotten_oranges.popleft()
            for dr, dc in displacements:
                row, column = r + dr, c + dc
                if 0 <= row < rows and 0 <= column < columns and grid[row][column] == 1:
                    grid[row][column] = 2
                    rotten_oranges.append((row, column))
                    fresh -= 1
        minutes += 1

    return minutes if fresh == 0 else -1


if __name__ == '__main__':
    print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
    print(oranges_rotting([[1], [2], [1], [2]]))
