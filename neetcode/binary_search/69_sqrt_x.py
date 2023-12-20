def my_sqrt(x: int) -> int:
    left, right = 0, x
    result = 0

    while left <= right:
        middle = left + (right - left) // 2
        val = middle * middle

        if val > x:
            right = middle - 1
        elif val < x:
            left = middle + 1
            result = middle
        else:
            return middle

    return result


if __name__ == '__main__':
    inputs = [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (17, 4),
        (24, 4),
        (25, 5),
    ]
    for input_ in inputs:
        print(my_sqrt(input_[0]) == input_[1])
