def check_valid_string(s: str) -> bool:
    # TODO resolve later
    left_min, left_max = 0, 0

    for c in s:
        if c == "(":
            left_min, left_max = left_min + 1, left_max + 1
        elif c == ")":
            left_min, left_max = left_min - 1, left_max - 1
        else:
            left_min, left_max = left_min - 1, left_max + 1
        if left_max < 0:
            return False
        if left_min < 0:
            left_min = 0
    return left_min == 0


if __name__ == '__main__':
    print(check_valid_string('(*))'))
