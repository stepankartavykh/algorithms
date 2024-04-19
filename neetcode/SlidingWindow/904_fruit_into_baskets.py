import collections


def total_fruit(fruits: list[int]) -> int:
    res = 0
    count = collections.defaultdict(int)
    total = 0
    left = 0
    for right in range(len(fruits)):
        count[fruits[right]] += 1
        total += 1

        while len(count) > 2:
            total -= 1
            count[left_fruit_type] -= 1
            left += 1
            if not count[left_fruit_type]:
                count.pop(left_fruit_type)

        res = max(res, total)

    return res


if __name__ == '__main__':
    print(total_fruit([1, 2, 1]))
    print(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
