# a, b, c, d = list(map(int, input().split()))


def test_main():
    assert main(1, 2, 1, 2) == (1, 1)


def main(a, b, c, d):
    up = a * d + b * c
    down = b * d
    k = 1
    while True:
        k += 1
        while up % k == 0 and down % k == 0:
            down //= k
            up //= k
    print(up, down)
    return up, down


if __name__ == '__main__':
    test_main()
