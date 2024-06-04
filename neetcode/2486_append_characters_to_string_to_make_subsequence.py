

def append_characters(s: str, t: str) -> int:
    first, second = 0, 0
    # for ss, st in zip(s, t):
    while first < len(s) and s[first] != t[0]:
        first += 1
    if first == 0:
        return len(t)
    if first > len(s):
        return len(t)
    while True:
        if s[first] == t[second]:
            first += 1
            second += 1
        else:
            break

    return len(t) - second


if __name__ == '__main__':
    # print(append_characters("coaching", "coding"))
    # print(append_characters("abcde", "a"))
    print(append_characters("z", "abcde"))
