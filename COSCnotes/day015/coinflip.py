# coinflip.py

# simulated coin flip.
# give heads 1/2 time, tails 1/2 time

import random

def flip():
   return random.randint(0, 1) # either 0 or 1

headcount = 0.0
tailcount = 0.0

trials = 20000000

for i in range(trials):
    if flip() == 1:
        headcount += 1
    else:
        tailcount += 1
        
print headcount/trials, "heads"
print tailcount/trials, "tails"
