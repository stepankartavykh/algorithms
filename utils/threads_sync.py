"""
Code from article: https://habr.com/ru/articles/764420/
"""

import threading


class Counter:
    def __init__(self):
        self.val = 0

    def change(self):
        self.val += 1
        # second variant
        # self.val += int(1)


class ThreadsSafeCounter:
    def __init__(self):
        self.val = 0
        self.lock = threading.Lock()

    def change(self):
        with self.lock:
            self.val += 1


def work(counter, operations_count):
    for _ in range(operations_count):
        counter.change()


def run_threads(counter, threads_count, operations_per_thread_count):
    threads = []

    for _ in range(threads_count):
        t = threading.Thread(target=work, args=(counter, operations_per_thread_count))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == "__main__":
    threadsCount = 10
    operationsPerThreadCount = 1000000
    expectedCounterValue = threadsCount * operationsPerThreadCount
    counters = [Counter()]

    for counter in counters:
        run_threads(counter, threadsCount, operationsPerThreadCount)
        print(f"{counter.__class__.__name__}: expected val: {expectedCounterValue}, actual val: {counter.val}")