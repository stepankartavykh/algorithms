from typing import List


def generate_parenthesis(n: int) -> List[str]:
    result = []

    stack = []

    def backtracking(open_number, closed_number):
        if open_number == closed_number == n:
            result.append(''.join(stack))
            return
        if open_number < n:
            stack.append('(')
            backtracking(open_number + 1, closed_number)
            stack.pop()
        if open_number > closed_number:
            stack.append(')')
            backtracking(open_number, closed_number + 1)
            stack.pop()
    return result
