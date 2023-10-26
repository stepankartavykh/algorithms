def valid_palindrome(s: str) -> bool:

    left, right = 0, len(s) - 1
    flag_one_symbol = False
    while left < right:
        if flag_one_symbol:
            return False
        if s[left] != s[right]:
            flag_one_symbol = True

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    print(valid_palindrome('aba') is True)
    print(valid_palindrome('abca') is True)
    print(valid_palindrome('abc') is False)
