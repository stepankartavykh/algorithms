from typing import List


def eval_rpn(tokens: List[str]) -> int:
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }
    stack = []

    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            second = stack.pop()
            first = stack.pop()
            res = operations[token](first, second)
            stack.append(res)

    return stack[0]


if __name__ == '__main__':
    inputs = [
        ["18"],
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]
    for input_ in inputs:
        print(eval_rpn(input_))
