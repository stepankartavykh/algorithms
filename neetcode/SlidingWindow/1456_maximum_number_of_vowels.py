def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = 0
    print(len(s) - k)
    for i in range(0, len(s) - k + 1):
        temp = 0
        for j in range(0, k):
            if s[i + j] in vowels:
                temp += 1
        res = max(res, temp)
    return res

# TODO why second approach is faster? How str.count is working?

def maxVowelsSecond(s: str, k: int) -> int:
    max_count,counter=0,0
    for i in range(len(s)-k+1):
        string = s[i:k]
        counter = string.count('a') + string.count('e') + string.count('i')+string.count('o')+string.count('u')
        k+=1
        max_count=max(max_count,counter)
    return max_count


if __name__ == '__main__':
    print(maxVowels('weallloveyou', 7))