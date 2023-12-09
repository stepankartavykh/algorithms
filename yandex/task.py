from collections import deque


def convert_string_specific_way(input_string: str) -> str:
    words = input_string.split(' ')
    result = ''

    for word in words:
        result_word = ''
        word_lower_case = word.lower()
        for symbol in result_word:
