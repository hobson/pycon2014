# file: numba_pi_no_change.py

"""Calculating pi with Monte Carlo using numba. No changes.
"""

import math
import random
import sys

import numba

sys.path.append('../measuring')

import measure_time
import numba_no_debug


@numba.jit('float64(int64)')
def pi_numba(total):
    """Calculate pi with numba.
    """
    count_inside = 0
    for _ in range(total):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x * x + y * y)
        if dist < 1:
            count_inside += 1
    return 4.0 * count_inside / total


@numba.autojit
def pi_numba_auto(total):
    """Calculate pi with numba.
    """
    count_inside = 0
    for _ in range(total):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x * x + y * y)
        if dist < 1:
            count_inside += 1
    return 4.0 * count_inside / total


def pi(total):
    """Calculate pi with numba.
    """
    count_inside = 0
    for _ in xrange(total):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x * x + y * y)
        if dist < 1:
            count_inside += 1
    return 4.0 * count_inside / total


jitted_pi = numba.jit('float64(int64)')(pi)


jitted_pi_auto = numba.autojit(pi)


if __name__ == '__main__':

    def test():
        """Time the execution.
        """
        names = ['pi', 'pi_numba_auto', 'pi_numba', 'jitted_pi',
                 'jitted_pi_auto']
        measure_time.measure_run_time(int(1e6), names, number=3)
    test()
