def is_subsequence(s: str, t: str) -> bool:
    s_index, t_index = 0, 0
    if s == '':
        return True
    while t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
        if s_index == len(s):
            return True
    return False


def is_subsequence_second(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


if __name__ == '__main__':
    print(is_subsequence(s="abc", t="ahbgdc") == True)
    print(is_subsequence(s="axc", t="ahbgdc") == False)
    print(is_subsequence(s="acb", t="ahbgdc") == False)
    print(is_subsequence(s="", t="ahbgdc") == True)
