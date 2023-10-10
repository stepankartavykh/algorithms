def is_valid(s: str) -> bool:
    brackets = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    stack = []
    for symbol in s:
        if symbol in brackets:
            if stack and stack[-1] == brackets[symbol]:
                stack.pop()
            else:
                return False
        else:
            stack.append(symbol)
    return True if not stack else False


if __name__ == '__main__':
    print(is_valid('()[]{}'))
    print(is_valid('()'))
    print(is_valid('(}'))
