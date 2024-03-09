def partition(s: str) -> list[list[str]]:
    result = []
    current_partition = []

    def backtrack(i):
        if i >= len(s):
            result.append(current_partition.copy())
            return

        for j in range(i, len(s)):
            is_palindrome = True
            left, right = i, j
            while left < right:
                if s[left] != s[right]:
                    is_palindrome = False
                left += 1
                right -= 1
            if is_palindrome:
                current_partition.append(s[i:j + 1])
                backtrack(j + 1)
                current_partition.pop()

    backtrack(0)
    return result


if __name__ == '__main__':
    print(partition('aab'))
    print(partition('abcddcba'))
    print(partition('efe'))
