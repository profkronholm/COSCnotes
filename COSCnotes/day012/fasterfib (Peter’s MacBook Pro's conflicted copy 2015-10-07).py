# fasterfib.py
# Bill Kronholm
# 2015
#
# A program to compute the Fibonacci numbers, quickly using a recursive function.

import sys
sys.setrecursionlimit(10000)
fibonacci = {0:0, 1:1} # initial values

def getfib(n):
    if n in fibonacci:
        return fibonacci[n]
    else:
        fibonacci[n] = getfib(n-1) + getfib(n-2)
        return fibonacci[n]

print getfib(9999
