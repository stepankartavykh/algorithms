from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    # TODO bad solution! Time complexity evaluation is horrible!
    for position in range(len(s2) - len(s1) + 1):
        string = s2[position:position+len(s1)]
        if Counter(string) == Counter(s1):
            return True
    return False


if __name__ == '__main__':
    print(check_inclusion('ab', 'eidbaooo') is True)
    print(check_inclusion('ab', 'eidaooo') is False)
    print(check_inclusion('hello', 'ooolleoooleh') is False)
