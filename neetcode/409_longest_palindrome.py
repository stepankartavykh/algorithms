import dis
import timeit
from collections import defaultdict
from typing import Callable


def longest_palindrome(s: str) -> int:
    letters_count = defaultdict(int)
    for symbol in s:
        letters_count[symbol] += 1
    res = 0
    ones = 0
    for count in letters_count.values():
        if count % 2 == 0:
            res += count
        else:
            res += (count - 1)
            ones += 1
    if ones > 0:
        res += 1
    return res


def nice_solution(s: str) -> int:
    seen = set()
    res = 0
    for symbol in s:
        if symbol in seen:
            seen.remove(symbol)
            res += 2
        else:
            seen.add(symbol)
    if seen:
        return res + 1
    return res


def compare_two_functions(first: Callable, second: Callable) -> None:
    """
    :param first: function to measure execution time
    :param second: function to measure execution time
    """
    pass


if __name__ == '__main__':
    execution_time_first = timeit.timeit(code_first, number=1000)
    execution_time_second = timeit.timeit(code_second, number=1000)
    print(execution_time_first)
    print(execution_time_second)
