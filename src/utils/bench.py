import time
from functools import wraps


def bench(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        total_time_ms = (end_time - start_time) * 1000
        print(f"Function {func.__name__} took {total_time_ms:.2f}ms")

        return result

    return timeit_wrapper
