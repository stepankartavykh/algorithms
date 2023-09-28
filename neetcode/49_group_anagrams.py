from collections import Counter
from typing import List


def test_leet_code_cases(solution_function):
    assert solution_function(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert solution_function([""]) == [[""]]
    assert solution_function(["a"]) == [["a"]]
    print('all tests passed!')


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = []
    for i in range(len(strs)):
        one_anagram = [strs[i]]
        for j in range(i + 1, len(strs)):
            if Counter(strs[i]) == Counter(strs[j]):
                one_anagram.append(strs[j])

        anagrams.append(one_anagram)
    return anagrams


def group_anagrams_second_solution(s: str, t: str) -> bool:
    pass


def test_hypothesis():
    # TODO MUST BE RESOLVED! There is no understanding of variable 'i' behaviour.
    arr = list(range(10))
    for i in range(len(arr)):
        if i % 2 == 0:
            arr.remove(arr[i])
            i -= 1
        else:
            print(arr[i])


if __name__ == '__main__':
    test_hypothesis()
    # test_leet_code_cases(group_anagrams)
