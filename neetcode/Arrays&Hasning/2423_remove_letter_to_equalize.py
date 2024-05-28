from collections import Counter


def equal_frequency(word: str) -> bool:
    letter_to_count = Counter(word)

    if len(letter_to_count.values()) == 1:
        return True

    if all(val == 1 for val in letter_to_count.values()):
        return True

    counter_to_count = Counter(letter_to_count.values())
    if len(counter_to_count.values()) != 2:
        return False

    item1, item2 = counter_to_count.items()
    if item1 > item2:
        item1, item2 = item2, item1
    if item2[0] - item1[0] == 1 and item2[1] == 1:
        return True

    if item1 == (1, 1):
        return True

    return False
