import heapq
from collections import Counter, deque


def leastInterval(tasks: list[str], n: int) -> int:
    # TODO Resolve later!
    """
    we use heap data structure so that tasks[0] will be maximum of specific task. e.g.
    "AAAABBBCCD" - in this example number of A must be first
    """
    tasks = [-cnt for cnt in Counter(tasks).values()]
    heapq.heapify(tasks)

    time = 0
    tasks_with_idle = deque()
    while tasks or tasks_with_idle:
        """each iteration time counter must be incremented"""
        time += 1

        if not tasks:
            # so there is value in q. extract it
            time = tasks_with_idle[0][1]
        else:
            # add 1 to idle time of one task type
            new_idle_time = 1 + heapq.heappop(tasks)
            if new_idle_time:  # if idle time == 0, which means all tasks for on type finished, then nothing
                tasks_with_idle.append([new_idle_time, time + n])
        if tasks_with_idle and tasks_with_idle[0][1] == time:
            # there is something in queue, so we need to add it to tasks counter
            heapq.heappush(tasks, tasks_with_idle.popleft()[0])
    return time


def get_all_combos(nums: list[int]):
    # numbers = [-q for q in nums]
    numbers = nums.copy()
    heapq.heapify(numbers)

    while len(numbers):
        copy_numbers = numbers.copy()
        heapq.heappop(numbers)
        print(copy_numbers, numbers)


if __name__ == '__main__':
    inputs = [
        # [3, 4, 1, 5],
        # [3, 3, 1, 3],
        [3, 2, 1, 4, 2, 5, 1, -1]
    ]
    for inp in inputs:
        get_all_combos(inp)
