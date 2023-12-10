from string import punctuation


def test_function(func):
    input_data = 'Привет! Давно не виделись.'
    right_answer = 'Тевирп! Онвад ен ьсиледив.'
    answer = func(input_data)
    assert answer == right_answer, answer


def reverse_word(string) -> str:
    reversed_string = [''] * len(string)
    for position in range(len(string)):
        if string[position] in punctuation:
            reversed_string[position] = string[position]
        else:
            reversed_string[position]


def convert_string_specific_way(input_string: str) -> str:
    words = input_string.split(' ')
    reversed_words = []
    counter_white_spaces = 0
    for word in words:
        if len(word):
            if counter_white_spaces:
                reversed_words.append(' ' * (counter_white_spaces + 1))
                counter_white_spaces = 0
            reversed_words.append(reverse_word(word))
        else:
            counter_white_spaces += 1
    return ''.join(reversed_words)


if __name__ == '__main__':
    test_function(convert_string_specific_way)
