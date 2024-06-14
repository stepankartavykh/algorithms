def min_increment_for_unique(nums: list[int]) -> int:
    nums.sort()
    res = 0
    current = 0
    for num in nums:
        current = max(current, num)
        res += current - num
        current += 1
    return res


def min_increment_for_unique_linear(nums: list[int]) -> int:
    min_n = min(nums)
    cnt = [0] * (max(nums) - min_n + len(nums))
    for n in nums:
        cnt[n - min_n] += 1
    step, total = 0, 0
    for c in cnt:
        step += c
        if step > 0:
            step -= 1
        total += step
    return total


def generate_tests() -> list[list[int]]:
    pass


if __name__ == '__main__':
    print(min_increment_for_unique([3, 2, 1, 2, 1, 7]))
