def test_leet_code_cases(solution_function):
    assert solution_function("anagram", "nagaram") == 1, '1'
    assert solution_function("rat", "car") == 0, '2'
    print('all tests passed!')


def is_anagram(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)


def is_anagram_second_solution(s: str, t: str) -> bool:
    pass


if __name__ == '__main__':
    test_leet_code_cases(is_anagram)
