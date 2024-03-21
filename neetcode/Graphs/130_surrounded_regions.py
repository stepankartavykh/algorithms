def solve(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r == m or c == n or board[r][c] != "O":
            return
        board[r][c] = "N"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(m):
        for c in range(n):
            if r == 0 or r == m - 1 or c == 0 or c == n - 1 and board[r][c] == 'O':
                dfs(r, c)

    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            if board[r][c] == 'N':
                board[r][c] = 'O'
