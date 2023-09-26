# TODO figure out how to compare execution time for some module
import timeit


class A:
    def __init__(self, x):
        self.x = x
    
    def __eq__(self, other):
        return other.x == self.x

    def __lt__(self, other):
        return other.x <= self.x


def test_execution_time():
    a = A(1)
    b = A(2)
    c = a != b
    c = a < b


def code_sample():
    for i in range(10):
        test_execution_time()


if __name__ == '__main__':
    print(timeit.timeit(code_sample))
