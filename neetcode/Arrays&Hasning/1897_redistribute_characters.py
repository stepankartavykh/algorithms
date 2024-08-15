from collections import Counter


def make_equal(words: list[str]) -> bool:
    if len(words) == 1:
        return True
    total_word = ''.join(words)
    if len(total_word) % len(words) != 0:
        return False
    letter_counter = Counter(total_word)
    letters_count = len(letter_counter)
    first = list(letter_counter.values())[0]
    return letters_count == first


if __name__ == '__main__':
    print(make_equal(['abc', 'aabc', 'bc']) is True)
    print(make_equal(['ab', 'a']) is False)
    print(make_equal(['a', 'b']) is False)
    print(make_equal(['asdf']) is True)
    print(make_equal(["a", "a", "a"]) is True)
