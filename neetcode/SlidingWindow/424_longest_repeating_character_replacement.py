from string import ascii_uppercase


def character_replacement(s: str, k: int) -> int:
    d = {}
    for letter in ascii_uppercase:
        d[letter] = 0

    left, right = 0, 0
    result = 0
    while right < len(s):

        d[s[right]] += 1
        window_length = right - left + 1
        most_common_count = max(d.values())
        if window_length - most_common_count <= k:
            result = window_length
        else:
            d[s[left]] -= 1
            left += 1

        right += 1

    return result


if __name__ == '__main__':
    print(character_replacement(s="ABAB", k=2))
    print(character_replacement(s="AABABBA", k=1))
