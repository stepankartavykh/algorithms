def num_decodings(s: str) -> int:
    if len(s) == 0:
        return 1
    elif s[0] == '0':
        return 0
    elif len(s) == 1:
        return 1
    else:
        if int(s[:2]) <= 26:
            return num_decodings(s[1:]) + num_decodings(s[2:])
        else:
            return num_decodings(s[1:])


def num_decodings_dp(s: str) -> int:
    cached = {len(s): 1}

    def number_of_ways_from_position(i):
        if i in cached:
            return cached[i]
        if s[i] == '0':
            return 0

        current_number_ways = number_of_ways_from_position(i + 1)
        if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
            current_number_ways += number_of_ways_from_position(i + 2)
        cached[i] = current_number_ways
        return current_number_ways

    return number_of_ways_from_position(0)


def bruteforce(s: str) -> int:
    # TODO Memory Limit Exceeded!
    ways = []
    current = []

    def backtrack(i):
        if i >= len(s):
            ways.append(current.copy())
            return

        if s[i] in '123456789':
            current.append(s[i])
            backtrack(i + 1)
            current.pop()
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                current.append(s[i] + s[i + 1])
                backtrack(i + 2)

    backtrack(0)

    return len(ways)


def num_decodings_dp_second(s: str) -> int:
    if s[0] == '0':
        return 0

    first = 1
    second = 1

    for i in range(1, len(s)):
        current = 0

        if s[i] != '0':
            current += first

        two_digit = int(s[i - 1:i + 1])
        if 10 <= two_digit <= 26:
            current += second

        second = first
        first = current

    return first


if __name__ == '__main__':
    print(num_decodings_dp('111111111111111111111111111111111111111111111'))
    print(num_decodings_dp('1'))
    print(num_decodings_dp('12'))
    print(num_decodings_dp('226'))
    print(num_decodings_dp('06'))
    print(num_decodings_dp('906'))
    print(num_decodings_dp('12345'))
