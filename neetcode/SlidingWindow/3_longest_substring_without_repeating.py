


def lengthOfLongestSubstring(s: str) -> int:
    left, right = 0, len()

    while left < right:

        if right < len(s) and s[right] not in s[left:right]:
            right += 1
        else:
            left += 1

    return right - left

if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    