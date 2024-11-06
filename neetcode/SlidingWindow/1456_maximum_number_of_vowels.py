from collections import deque

from data_1456 import timeout_string
from utils.func import timeit


@timeit
def max_vowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = 0
    window = deque(s[:k])
    for symb in window:
        if symb in vowels:
            res += 1
    cur_count = res
    for i in range(k, len(s)):

        if window[0] in vowels:
            cur_count -= 1
        if s[i] in vowels:
            cur_count += 1
        window.popleft()
        window.append(s[i])
        res = max(res, cur_count)
    return res

# TODO why second approach is faster? How str.count is working?

@timeit
def max_vowels_second(s: str, k: int) -> int:
    max_count, counter = 0, 0
    for i in range(len(s) - k + 1):
        string = s[i:k]
        counter = string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')
        k += 1
        max_count = max(max_count, counter)
    return max_count


if __name__ == '__main__':
    print(max_vowels("weallloveyou", 7))
    print(max_vowels('leetcode', 3))
    print(max_vowels(timeout_string, 3945))
    print(max_vowels_second(timeout_string, 3945))
