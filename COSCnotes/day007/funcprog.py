# funcprog.py
# Bill Kronholm
# 2015
#
# Demonstrates some functional programming methods and list comprehensions.
#
#

#########################################
# Functional Programming

# filter
# used to filter a list with a boolean function
# returns a list


#def f(x):
#    return (x % 3 == 0) or (x % 7 == 0) # true for multiples of either 3 or 7

#tresSiete = filter(f, range(1,1000))
#print tresSiete

#tresSiete = []
#for n in range(1, 1000):
#    if f(n):
#        tresSiete.append(n)

# map
# used to apply a function to all elements of a list
# returns a list

#def g(x):
#    return 3*(x**2) + 2

#print map(g, [1, 2, 3, 4, 5])

#def add(x,y):
#    return x+y
#    
#print map(add, [2, 3, 4], [5, 3, 1])

# 

# reduce
# used to apply a function repeatedly to items in a list

def add(x,y):
    return x+y

print reduce(add, [3, 4, 5, 6, 7, 8, 9, 10])


############################################
# List comprehensions

#evens = [2*x for x in range(10)]
#print evens
#odds = [2*x + 1 for x in range(10)]
#print odds

#multfours = [2*x for x in range(10) if x%2 == 0]
#print multfours

#pairs = [ [x,y] for x in range(3) for y in range(4) ]
#print pairs



#differentpairs = [ [x,y] for x in range(3) for y in range(4) if x != y]
#print differentpairs









