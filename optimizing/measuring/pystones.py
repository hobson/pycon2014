#pystones.py

import time
import os
import timeit

def faste(N=100):
    e, x = 1, 1
    for i in xrange(N):
        x *= x
        e += 1./x
    return e

def slowe(N=100):
    e, x = 1, 1
    for i in range(N):
        x *= x
        e += 1./x
    return e

def fast():
    sleep(.001)

def slow():
    sleep(.01)

def sleep(t=2):
    time.sleep(t)


def accumulate(iterable):
    acm = [iterable[0]]
    for el in iterable[1:]:
        acm += [acm[-1] + el]
    return acm

#def calc(num, loops=1000):
