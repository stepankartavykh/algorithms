def max_score(s: str) -> int:
    s = list(map(int, s))
    res = 0
    for i in range(len(s) - 1):
        res = max(res, i + 1 - sum(s[0:i+1]) + sum(s[i+1:]))
    return res


if __name__ == '__main__':
    print(max_score('011101') == 5)
    print(max_score('00111') == 5)
    print(max_score('1111') == 3)
