def exist(board: list[list[str]], word: str) -> bool:
    # TODO: Where is TLE?
    rows = len(board)
    columns = len(board[0])
    first_letter = word[0]
    visited_letters = set()

    def traverse_board(r, c, i) -> bool:
        # If position (i) == length of the word, then path is found, hence return True.
        if i == len(word):
            return True
        # Check conditions: going beyond borders, compare letter word and board,
        # second visit of the same letter (which is prohibited)
        if r < 0 or c < 0 or r >= rows or c >= columns or board[r][c] != word[i] or (r, c) in visited_letters:
            return False
        # Add letter (cell on the board) in the "path" of letters, that are visited
        visited_letters.add((r, c))
        # Making next step on the board (in 4 directions)
        next_step = traverse_board(r + 1, c, i + 1) or traverse_board(r - 1, c, i + 1) or traverse_board(r, c + 1, i + 1) or traverse_board(r, c - 1, i + 1)
        # After we made 4 steps - delete visited cell
        visited_letters.remove((r, c))
        # return result of the next step
        return next_step

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == first_letter:
                if traverse_board(row, column, 0):
                    return True
    return False


if __name__ == '__main__':
    inputs = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
    ]
    for input_ in inputs:
        print(exist(input_[0], input_[1]))


# TODO form neetcode solution (https://github.com/neetcode-gh/leetcode/blob/main/python/0079-word-search.py):
#  What this piece of code is doing?
#  count = defaultdict(int, sum(map(Counter, board), Counter()))
#      if count[word[0]] > count[word[-1]]:
#          word = word[::-1]
