def is_palindrome(x: int) -> bool:
    new_x = 0
    x_copy = x
    while x_copy > 0:
        figure = x_copy % 10
        x_copy = x_copy // 10
        new_x = new_x * 10 + figure
    return x == new_x


if __name__ == '__main__':
    print(is_palindrome(121) is True)
    print(is_palindrome(10) is False)
    print(is_palindrome(1111111) is True)
    print(is_palindrome(1111121) is False)
    print(is_palindrome(-121) is False)
    print(is_palindrome(0) is True)
