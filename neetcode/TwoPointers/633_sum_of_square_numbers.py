import math


def judge_square_sum(c: int) -> bool:
    l, r = 0, round(math.sqrt(c))
    while l <= r:
        sum_ = l * l + r * r
        if sum_ == c:
            return True
        if sum_ < c:
            l += 1
        else:
            r -= 1
    return False
