# randomstuff.py
# Bill Kronholm
# 2015
#
# Demonstrates some usage of the random module

import random # 

#random.seed(1) # randomize the randomizer

#for i in range(10):
#    print random.random() # get a random float x with 0 <= x < 1


#for i in range(10):
#    print random.uniform(3, 5.5) # random float 3 <= x <= 5.5 (or maybe < 5.5)

#for i in range(10):
#    print random.randint(1,34) # random integer x with 1 <= x <= 34

#mylist = [random.randint(97, 122) for i in range(10)] # 10 random ints

#randomstring = ''.join([chr(x) for x in mylist]) # use chr to get characters
#print randomstring

#def getrandomstring(n, low = 97, high = 122):
#    """
#    Returns a string of n random characters.
#    Defaults to range for 8-bit characters corresponding to 'a' to 'z'.
#    (Hence default values of low = 97 and high = 122)
#    """
#    randchars = [chr(random.randint(low,high)) for i in range(n)]
#    return ''.join(randchars)

#for i in range(10):
#    print getrandomstring(i)

nicelist = range(20)
#print random.choice(nicelist) # one element chosen randomly
#print random.sample(nicelist, 3) # list of 3 randomly chosen elements. no replacement


random.shuffle(nicelist) # shuffles the list itself (not a copy)
print nicelist
