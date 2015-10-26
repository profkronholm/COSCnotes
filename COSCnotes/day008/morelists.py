# morelists.py
# Bill Kronholm
# 2015
#
# Demonstrates basic list comprehensions

############################################
# List comprehensions

#evens = [2*x for x in range(10)]
#print evens
#odds = [2*x + 1 for x in range(10)]
#print odds

#multfours = [x for x in range(10) if (x % 4 == 0) and (x != 0)]
#print multfours

#def isprime(n):
#    if n < 2:
#        return False
#    m = 2
#    while m < n:
#        if n % m == 0:
#            return False
#        m = m + 1
#    return True

#primes = [p for p in range(2,100) if isprime(p)]    
#print primes    

#n = 3456
#factors = [ x for x in range(1, n + 1) if n % x == 0]
#print factors
#pairs = [ [x, y] for y in range(4) for x in range(3)]
#print pairs



differentpairs = [ [x,y] for x in range(3) for y in range(4) if x != y]
print differentpairs

