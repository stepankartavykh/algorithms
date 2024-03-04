def longest_palindrome(s: str) -> str:
    # Bruteforce
    max_pal = s[0]
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            tmp_s = s[i:j + 1]
            if tmp_s == tmp_s[::-1] and len(max_pal) < j - i + 1:
                max_pal = tmp_s
    return max_pal


def longest_palindrome_second(s: str) -> str:
    max_pal = ''
    max_length = 0

    for i in range(len(s)):
        left, right = i, i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                max_pal = s[left:right + 1]
                max_length = right - left

            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                max_pal = s[left:right + 1]
                max_length = right - left

            left -= 1
            right += 1

    return max_pal


if __name__ == '__main__':
    print(longest_palindrome_second('a'))
    print(longest_palindrome_second('cc'))
    print(longest_palindrome_second('babad'))
    print(longest_palindrome_second('cbbd'))
    print(longest_palindrome_second('ccaaaaac'))
