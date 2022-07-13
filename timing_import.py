from time import perf_counter
from collections import namedtuple

Timings = namedtuple('Timing', 'timing_1 timing_2, abs_diff rel_diff_perc')

def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100

    timings = Timings(round(timing1, 1),
                      round(timing2, 1),
                      round(timing2 - timing1, 1),
                      round(rel_diff, 2))

    return timings

print(compare_timings(1, 2))

test_repeats = 10_000_000


#### Timing using fully qualified module.symbol

import math

start = perf_counter()

for _ in range(test_repeats):
    math.sqrt(2)

end = perf_counter()

elapsed_fully_qualified = end - start

print(f'Elapsed: {elapsed_fully_qualified}')

#### Timing using a directly import symbol name

from math import sqrt

start = perf_counter()

for _ in range(test_repeats):
    sqrt(2)

end = perf_counter()

elapsed_direct_symbol = end - start

print(f'Elapsed: {elapsed_direct_symbol}')

print(compare_timings(elapsed_fully_qualified, elapsed_direct_symbol))

#### Timing using a function wrapper (full qualified symbol)
import math

def func():
    math.sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_func_fully_qualified = end - start

print(f'Elapsed: {elapsed_func_fully_qualified}')

from math import sqrt

def func():
    sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_func_direct_symbol = end - start

print(f'Elapsed: {elapsed_func_direct_symbol}')

print(compare_timings(elapsed_func_fully_qualified, elapsed_func_direct_symbol))

#### Nested imports

def func():
    import math
    math.sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_nested_fully_qualified = end - start

print(f'Elapsed: {elapsed_nested_fully_qualified}')

print(compare_timings(elapsed_func_fully_qualified, elapsed_nested_fully_qualified))

def func():
    from math import sqrt
    sqrt(2)

start = perf_counter()

for _ in range(test_repeats):
    func()

end = perf_counter()

elapsed_nested_direct_symbol = end - start

print(f'Elapsed: {elapsed_nested_direct_symbol}')

print(compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol))
