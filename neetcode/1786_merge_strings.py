

def merge_words(word1, word2):
    string = ''
    len1 = len(word1)
    len2 = len(word2)
    length = min(len1, len2)

    index = 0
    while index < length:
        string += word1[index]
        string += word2[index]
        index += 1
    if len1 >= len2:
        string += word1[index:len1]
    else:
        string += word2[index:len2]

    return string


if __name__ == '__main__':
    print(merge_words('aaa', 'bbb'))
    print(merge_words('a', 'bbb'))
    print(merge_words('aaa', 'bb'))
    print(merge_words('aaa', ''))
    print(merge_words('', ''))