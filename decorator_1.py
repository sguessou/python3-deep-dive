import time
import functools
from functools import lru_cache
from time import perf_counter

def dec_factory(reps):
    def timed(fn):
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += perf_counter() - start

            avg_elapsed = total_elapsed / reps
            print(f'Avg Run time: {avg_elapsed:.6f}')
            return result
        return inner
    return timed

@lru_cache
def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)





@dec_factory(20)
def fib(n):
    return calc_fib_recurse(n)

fib(200)
