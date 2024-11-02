import dis
import random
import urllib.request
from typing import Callable


def io_operations_counter(function: Callable):
    def wrapper(*args, **kwargs):
        print('counter of I/O operations is working...')
        counter = 0
        result = function(*args, **kwargs)
        print(dis.get_instructions(function))
        instructions = dis.get_instructions(function)
        for instr in instructions:
            print(instr.argrepr)
        counter += random.randint(0, 10)
        print(f'I/O operations count: {counter}')
        return result

    return wrapper


@io_operations_counter
def test_func():
    print('qwe')
    urllib.request.urlopen('http://www.python.org/')


def parse_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='HOST', type=str,
                        help=f'Specify server address [default: HOST]')
    parser.add_argument('--port', default='PORT', type=int,
                        help=f'Specify alternate port [default: PORT]')

    return parser.parse_args()


if __name__ == '__main__':
    test_func()