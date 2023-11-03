# a, b, c, d = list(map(int, input().split()))
import math


def test_main():
    assert main(1, 1, 1, 1) == (2, 1)
    assert main(1, 2, 1, 2) == (1, 1)
    assert main(1, 2, 1, 3) == (5, 6)
    assert main(3, 4, 7, 2) == (17, 4)
    assert main(1, 3, 1, 3) == (2, 3)
    assert main(1, 3, 1, 4) == (7, 12)
    assert main(1, 4, 3, 4) == (1, 1)
    assert main(7, 11, 2, 11) == (9, 11)
    assert main(7, 11, 5, 11) == (12, 11)


def main(a, b, c, d):
    up = a * d + b * c
    down = b * d

    k = 2
    max_divisor = max(b, d)
    while k <= max_divisor:
        if up % k == 0 and down % k == 0:
            down //= k
            up //= k
        else:
            k += 1

    print(up, down)

    return up, down


if __name__ == '__main__':
    test_main()
