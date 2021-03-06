# primes.py
# Bill Kronholm
# 2015
#
# A program to find all primes smaller than any given positive integer.
#

# returns True if n is prime, otherwise returns False.
# Note: returns True if n = 1 or 0. Fix it!
def isprime(n):
    if n < 2:
        return False
    m = 2
    while m < n:
        if n % m == 0:
            return False
        m = m + 1
    return True
    
myinteger = raw_input('Please enter an integer: ')
myinteger = int(myinteger)

listofints = range(myinteger+1) # check these for primality

knownprimes = [] # used to accumulate prime numbers

for i in listofints:
    if isprime(i):
        knownprimes.append(i)

#print "The primes up to " + str(myinteger) + " are:"
print "The primes up to %d are:" % myinteger # myinteger is inserted for the %d
allprimes = str(knownprimes)
print allprimes[1:-1]


#print isprime(myinteger)

####
