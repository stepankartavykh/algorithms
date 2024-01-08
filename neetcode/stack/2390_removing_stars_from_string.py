def remove_stars(s: str) -> str:
    stack = []
    for symbol in s:
        if symbol != '*':
            stack.append(symbol)
        else:
            stack and stack.pop()
    return ''.join(stack)


if __name__ == '__main__':
    print(remove_stars("leet**cod*e"))
    print(remove_stars("erase*****"))
