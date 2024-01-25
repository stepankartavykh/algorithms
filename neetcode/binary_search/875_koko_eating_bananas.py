from math import ceil
from typing import List


def min_eating_speed_bruteforce_solution(piles: List[int], h: int) -> int:
    k_speed = sum(piles) // h if sum(piles) > h else 1
    while True:
        count_hours = 0
        speed_should_be_more = False
        for pile in piles:
            hours_to_eat_all_pile = (pile // k_speed + 1) if pile % k_speed != 0 else pile // k_speed
            count_hours += hours_to_eat_all_pile
            if count_hours > h:
                speed_should_be_more = True
                break
        if speed_should_be_more:
            k_speed += 1
        else:
            return k_speed


def min_eating_speed(piles: List[int], h: int) -> int:
    # TODO Resolve this!
    left, right = 1, max(piles)
    min_speed = right

    while left <= right:
        speed = (left + right) // 2

        count_hours = 0
        for pile in piles:
            count_hours += ceil(pile / speed)

        if count_hours <= h:
            min_speed = min(speed, min_speed)
            right = speed - 1
        else:
            left = speed + 1

    return min_speed


if __name__ == '__main__':
    inputs = [
        ([3, 6, 7, 11], 8,),
        ([30, 11, 23, 4, 20], 5),
        ([30, 11, 23, 4, 20], 6),
        ([1000000000, 1000000000], 3),
        ([1, 1, 1, 999999999], 10),
    ]
    for input_ in inputs:
        print(min_eating_speed(input_[0], input_[1]))
