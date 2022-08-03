import timing_2

code = '[x**2 for x in range(1_000)]'

result = timing_2.timeit(code, 10)
print(result)
