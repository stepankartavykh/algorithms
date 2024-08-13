def is_path_crossing(path: str) -> bool:
    visited = {(0, 0)}
    cur_x, cur_y = 0, 0

    for move in path:
        if move == 'N':
            cur_y += 1
        elif move == 'S':
            cur_y -= 1
        elif move == 'E':
            cur_x += 1
        elif move == 'W':
            cur_x -= 1
        if (cur_x, cur_y) in visited:
            return True
        visited.add((cur_x, cur_y))

    return False


if __name__ == '__main__':
    print(is_path_crossing('NESWW'))
