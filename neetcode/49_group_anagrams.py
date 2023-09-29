from collections import Counter, defaultdict
from typing import List


def test_leet_code_cases(solution_function):
    # TODO make function to get all permutations for lists in list to make assert statement below
    assert solution_function(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert solution_function([""]) == [[""]]
    assert solution_function(["a"]) == [["a"]]
    print('all tests passed!')


def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = []
    i = 0
    while i < len(strs):
        one_anagram = [strs[i]]
        j = i + 1
        while j < len(strs):
            if Counter(strs[i]) == Counter(strs[j]):
                one_anagram.append(strs.pop(j))
                j -= 1
            j += 1
        anagrams.append(one_anagram)
        i += 1
    return anagrams


def group_anagrams_second_solution(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


def group_anagrams_third_solution(strs: List[str]) -> List[List[str]]:
    answer = {}
    for word in strs:
        counter_arr = [0] * 26
        for symbol in word:
            counter_arr[ord(symbol) - ord('a')] += 1
        if tuple(counter_arr) not in answer:
            answer[tuple(counter_arr)] = [word]
        else:
            answer[tuple(counter_arr)].append(word)
    return list(answer.values())


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
    # print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(group_anagrams([""]))
    # print(group_anagrams(["a"]))
    # print(group_anagrams(["", ""]))
    # print(group_anagrams(["", "", ""]))

    print(group_anagrams_second_solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams_second_solution([""]))
    print(group_anagrams_second_solution(["a"]))
    print(group_anagrams_second_solution(["", ""]))
    print(group_anagrams_second_solution(["", "", ""]))

    # test_leet_code_cases(group_anagrams)
