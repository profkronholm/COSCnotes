# directfib.py
# Bill Kronholm
# 2015
#
# A program to compute the Fibonacci numbers directly.

from math import sqrt

def getfib(n):
    phi = (1 + sqrt(5))/2
    psi = 1 - phi
    return (phi**n - psi**n)/sqrt(5)

print getfib(1000)

