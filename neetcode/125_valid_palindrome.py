def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    s_length = len(s)
    for position in range(s_length // 2):
        if s[position] != s[s_length - position - 1]:
            return False
    return True


def is_letter_or_figure(symbol) -> bool:
    return (
        ord('A') <= ord(symbol) <= ord('Z') or
        ord('a') <= ord(symbol) <= ord('z') or
        ord('0') <= ord(symbol) <= ord('9')
    )


def is_palindrome_second(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not is_letter_or_figure(s[left]):
            left += 1
        while right > left and not is_letter_or_figure(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left, right = left + 1, right - 1
    return True
