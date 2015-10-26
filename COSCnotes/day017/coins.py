# coins.py
# Bill Kronholm
# 2015
#
# Some functions with flippling coins
#


def fixprob(prob):
    """
    makes sure prob is between 0 and 1
    """
    try:
        if prob > 1:
            return 1.0
        elif prob < 0:
            return 0.0
        else:
            return float(prob)
    except:
        return 0.0


def flip(headprob = 0.5):
    """
    simulated coin flip. returns 'H' with probability headprob.
    """
    from random import random # random() is a float between 0 and 1
    headprob = fixprob(headprob)
    if random() < headprob:
        return 'H'
    else:
        return 'T'

def multiflip(trials = 2, headprob = 0.5):
    """
    flips a coin multiple times and returns the results
    """
    from random import random
    headprob = fixprob(headprob)
    results = [] # list to store the results
    for _ in range(trials):
        results.append(flip(headprob))
    return results[:]

if __name__ == '__main__':
    print flip()
