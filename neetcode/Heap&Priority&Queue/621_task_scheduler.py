import heapq
from collections import Counter


def least_interval(tasks: list[str], n: int) -> int:
    counts = [-t for t in Counter(tasks).values()]
    heapq.heapify(counts)

