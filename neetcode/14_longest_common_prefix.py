import os
from typing import List


def comp(first, second):
    pref = ''
    if first == '' or second == '':
        return pref
    else:
        i = 0
        while i < min(len(first), len(second)):
            if first[i] == second[i]:
                pref += first[i]
            else:
                break
            i += 1
    return pref


def longestCommonPrefix(strs: List[str]) -> str:
    longest_prefix = strs[0]
    for index in range(1, len(strs)):

        pref = ''
        if longest_prefix == '' or strs[index] == '':
            return pref
        else:
            i = 0
            while i < min(len(longest_prefix), len(strs[index])):
                if longest_prefix[i] == strs[index][i]:
                    pref += longest_prefix[i]
                else:
                    break
                i += 1

        longest_prefix = pref

    return longest_prefix


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    #
    # print("---'", comp('123', '1234'), "'---", sep='')
