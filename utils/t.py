import timeit

# Define the code that you want to measure the execution time for
code_first = """
a = 0
b = 1
for i in range(100000):
    a, b = b, a
"""

code_second = """
a = 0
b = 1
for i in range(100000):
    t = a
    a = b
    b = t
"""


execution_time_first = timeit.timeit(code_first, number=1000)
execution_time_second = timeit.timeit(code_second, number=1000)

print(execution_time_first)
print(execution_time_second)
