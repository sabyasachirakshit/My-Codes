# Determine profiling of Python programs.

# Program-

import cProfile


def sum():
    print(1+2)


cProfile.run('sum()')
