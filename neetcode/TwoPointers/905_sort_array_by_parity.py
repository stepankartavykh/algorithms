import dis
import cProfile
import random
import time
from typing import Callable


def sort_array_by_parity(nums: list[int]) -> list[int]:
    return sorted(nums, key=lambda element: element % 2 != 0)


def sort_array_by_parity_second_solution(nums: list[int]) -> list[int]:
    even, odd = [], []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd


def get_profiling_data(func: Callable):
    with cProfile.Profile() as profiler:
        func([random.randint(1, 100) for _ in range(1000)])
        profiler.dump_stats(f'/home/skartavykh/MyProjects/leetcode/tests/stats/{func.__name__}{time.time_ns()}.txt')


if __name__ == '__main__':
    print(dis.dis(sort_array_by_parity_second_solution))
    print('====================================')
    print(dis.dis(sort_array_by_parity))
