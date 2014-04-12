# file: numba_random.py

"""Random numbers with numba.
"""

from numba import autojit, jit, random

import numba_no_debug

STATE = random.state_p
PREC = 0xffffffff


@autojit
def rand_auto():
    """Create a pseudo random between (0, 1).
    """
    return random.rk_interval(PREC, STATE) / PREC


@jit('float64()')
def rand_jit():
    """Create a pseudo random between (0, 1).
    """
    return random.rk_interval(PREC, STATE) / PREC


def rand_no_jit():
    """Create a pseudo random between (0, 1).
    """
    return random.rk_interval(PREC, STATE) / PREC


rand = jit('float64()')(rand_no_jit)


if __name__ == '__main__':

    import timeit

    def test():
        """Time the execution.
        """
        for name in ['rand_no_jit', 'rand', 'rand_jit']:
            print name + ':',
            print timeit.timeit('{}()'.format(name),
                  'from numba_random import {}'.format(name))
    test()
