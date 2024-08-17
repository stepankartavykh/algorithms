import string


def title_to_number(column_title: str) -> int:
    count = len(string.ascii_uppercase)
    char_to_number = {
        char: i
        for i, char in enumerate(string.ascii_uppercase, start=1)
    }
    result = 0
    for i in range(len(column_title)):
        num = char_to_number[column_title[i]]
        result += num * (count ** (len(column_title) - i - 1))
    return result
