def guess(num, pick=10):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guess_number(n: int) -> int:
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2
        if guess(mid) < 1:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(guess_number(10))
