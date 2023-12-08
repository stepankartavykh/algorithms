def length_of_longest_substring(s: str) -> int:
    letters = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in letters:
            letters.remove(s[left])
            left += 1
        letters.add(s[right])
        result = max(result, right - left + 1)
    return result


if __name__ == '__main__':
    print(length_of_longest_substring(''))
    print(length_of_longest_substring('a'))
    print(length_of_longest_substring('abcabcbb'))
    print(length_of_longest_substring('bbbbb'))
    print(length_of_longest_substring('pwwkew'))
