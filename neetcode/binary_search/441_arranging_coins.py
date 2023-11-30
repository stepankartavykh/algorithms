def arrange_coins(self, n: int) -> int:
    left, right = 1, n

    result = 0

    while left < right:
        middle = (left + right) // 2
        middle_sum = middle * (middle + 1) // 2
        if middle_sum > n:
            right = middle - 1
        else:
            left = middle + 1
            result = max(middle, result)
    return left
