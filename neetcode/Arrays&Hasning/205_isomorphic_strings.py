def is_isomorphic(s: str, t: str) -> bool:
    accordance = {}
    for i in range(len(s)):
        if s[i] not in accordance:
            accordance[s[i]] = t[i]
        elif t[i] != accordance[s[i]]:
            return False
    if len(set(list(accordance.values()))) != len(accordance.values()):
        return False
    return True


if __name__ == '__main__':
    print(is_isomorphic('egg', 'add') is True)
    print(is_isomorphic('foo', 'bar') is False)
    print(is_isomorphic('paper', 'title') is True)
    print(is_isomorphic('badc', 'baba') is False)
    print(is_isomorphic('bbbaaaba', 'aaabbbba') is False)
