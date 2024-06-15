def make_good(s: str) -> str:
    symbols = list(s)
    i = 0
    while i < len(symbols) - 1:
        if i < 0:
            i = 0
        if len(symbols) > 1 and symbols[i].lower() == symbols[i + 1].lower() and symbols[i] != symbols[i + 1]:
            del symbols[i]
            del symbols[i]
            i -= 2
        i += 1
    return ''.join(symbols)


def make_good_second_approach(s: str) -> str:
    result = []
    for symbol in s:
        if not result:
            result.append(symbol)
        elif result and symbol.lower() == result[-1].lower() and symbol != result[-1]:
            result.pop()
        else:
            result.append(symbol)
    return ''.join(result)
