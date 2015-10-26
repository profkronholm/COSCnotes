# fib.py
# Bill Kronholm
# 2015
#
# A program to compute the Fibonacci numbers using a recursive function.

#logfile = open("fib.log", "w")

def getfib(n):
    """
    Function to compute the nth Fibonacci number via a recursion algorithm.
    """
    if n == 0:
        return 0 # f_0 = 0
    elif n == 1:
        return 1 # f_1 = 1
    else:
#        logfile.write("I need to compute f(%d) and f(%d)...\n" % (n-1, n-2))
        return getfib(n-1) + getfib(n-2) # f_n = f_(n-1) + f_(n-2)

print getfib(1000)

#logfile.close()
