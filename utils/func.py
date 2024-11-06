import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        args_string = 'ARGS: {'
        for arg in args:
            if isinstance(arg, str) and len(arg) > 10:
                args_string += arg[:10] + '...' + ', '
            else:
                args_string += str(arg)
        args_string += '}'
        print(f'Function {func.__name__} {args_string} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper