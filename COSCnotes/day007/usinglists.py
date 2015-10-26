# usinglists.py
# Bill Kronholm
# 2015
#
# Example code demonstrating some ways to use lists.
#

ghosts = ['Blinky', 'Pinky', 'Inky', 'Clyde'] # names of ghosts

# prints each ghost in the list
#for ghost in ghosts: 
#    print ghost

#numberOfGhosts = len(ghosts) # length of the list

## prints entry and location
#for i in range(numberOfGhosts):
#    print "%s is at location %d in the list" % (ghosts[i], i)

# enumerate the list
#for i, ghost in enumerate(ghosts):
#    print "%s is at location %d in the list" % (ghost, i)
  
# sort the list

ghosts.sort()
#print ghosts

# insert new ghost names

ghosts.insert(2, 'Casper')
ghosts.insert(2, 'Abraham Lincoln')
#print ghosts

# count ghosts

#print len(ghosts)

# find index of a ghost name
ghosts = ghosts * 2
n = ghosts.index('Casper')
fewerghosts = ghosts[n+1:]
m = fewerghosts.index('Casper')
#print m
# count number of occurances of a single ghost name

print ghosts.count('Casper')

