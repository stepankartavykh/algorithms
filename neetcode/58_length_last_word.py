def length_of_last_word(s: str) -> int:
    i = -1
    length = 0

    while i > -len(s) and s[i] == ' ':
        i -= 1
    while i >= -len(s) and s[i] != ' ':
        length += 1
        i -= 1
    return length


if __name__ == '__main__':
    print(length_of_last_word('Hello World'))
    print(length_of_last_word('a'))
    print(length_of_last_word('qwer'))
    print(length_of_last_word('qwer   '))
