def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    letter_word = {}
    if len(words) != len(pattern):
        return False
    for index, symbol in enumerate(pattern):
        if symbol not in letter_word:
            if words[index] in letter_word.values():
                return False
            letter_word[symbol] = words[index]
        if letter_word[symbol] != words[index]:
            return False
    return True


def word_pattern_neetcode_solution(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) != len(pattern):
        return False

    symbol_to_word = {}
    word_to_symbol = {}

    for symbol, word in zip(pattern, words):
        if symbol in symbol_to_word and symbol_to_word[symbol] != word:
            return False
        if word in word_to_symbol and word_to_symbol[word] != symbol:
            return False
        symbol_to_word[symbol] = word
        word_to_symbol[word] = symbol
    return True


if __name__ == '__main__':
    print(word_pattern(pattern='abba', s='dog dog dog dog'))
