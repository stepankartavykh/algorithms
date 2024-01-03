from collections import Counter


def max_number_of_balloons(text: str) -> int:
    required_distribution = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    word_letters = set('balloon')
    text_letters = Counter(text)
    max_possible = len(text)

    for letter, count in text_letters.items():
        if letter in word_letters:
            required_count = required_distribution[letter]
            max_possible = min(max_possible, count // required_count)
            word_letters.remove(letter)

    return 0 if len(word_letters) > 0 else max_possible


def max_number_of_balloons_neetcode_solution(text: str) -> int:
    required_distribution = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    text_letters = Counter(text)

    max_possible = len(text)
    for letter in required_distribution:
        max_possible = min(max_possible, text_letters[letter] // required_distribution[letter])

    return max_possible


if __name__ == '__main__':
    # print(max_number_of_balloons_neetcode_solution('balloonballon'))
    # print(max_number_of_balloons_neetcode_solution('loonbalxballpoon'))
    # print(max_number_of_balloons_neetcode_solution('xxlloo'))
    print(max_number_of_balloons_neetcode_solution('xxqqq'))
