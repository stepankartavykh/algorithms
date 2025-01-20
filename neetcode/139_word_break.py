from collections import defaultdict


def word_break(s: str, word_dict: list[str]) -> bool:
    letter_to_words = defaultdict(list)
    for w in word_dict:
        letter_to_words[w[0]].append(w)

    all_results = set()

    def traverse(cur_string_index) -> bool:
        if cur_string_index > len(s):
            return False
        if cur_string_index == len(s):
            return True

        for word in letter_to_words[s[cur_string_index]]:
            if s[cur_string_index:].startswith(word):
                all_results.add(traverse(cur_string_index + len(word)))

        return any(all_results)

    return traverse(0)


if __name__ == '__main__':
    print(word_break(s="leetcode", word_dict=["leet", "code"]))
    print(word_break(s="applepenapple", word_dict=["apple", "pen"]))
    print(word_break(s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"]))
    print(word_break(s="cars", word_dict=["car", "ca", "rs"]))
    # TODO: fix TLE (dynamic programming)
    print(word_break(s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                     word_dict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
