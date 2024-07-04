def backspace_compare(s: str, t: str) -> bool:
    first = []
    for symbol in s:
        if symbol != '#':
            first.append(symbol)
        elif first:
            first.pop()
    second = []
    for symbol in t:
        if symbol != '#':
            second.append(symbol)
        elif second:
            second.pop()
    return ''.join(first) == ''.join(second)


if __name__ == '__main__':
    print(backspace_compare('xywrrmp', 'xywrrmu#p'))
