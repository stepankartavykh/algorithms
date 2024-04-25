import re


def longest_nice_substring(s: str) -> str:
    res = ''
    max_length = 0
    m = {s: s.upper() for s in 'abcdefghijklmnopqrstuvwxyz'}
    for q in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        m[q] = q.lower()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            print('============== DEBUG:', substring)
            unique_symbols = set(substring)
            for symb in unique_symbols:
                if m[symb] not in unique_symbols:
                    break
            else:
                if len(substring) > max_length:
                    max_length = len(substring)
                    res = substring
    return res


def longest_nice_substring_second(s: str) -> str:
    alone = set(s) - set(s.swapcase())
    if not alone:
        return s
    parts = re.split(f'[{"".join(alone)}]', s)
    print(parts)
    return max(map(longest_nice_substring_second, parts), key=len)


if __name__ == '__main__':
    print(longest_nice_substring_second('YazaAay'))
    print(longest_nice_substring_second('Bb'))
    print(longest_nice_substring_second('c'))
