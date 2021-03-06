# histogram.py
# Bill Kronholm
# 2015
#
# Prompts the user for a word and creates a hisogram of the frequency of 
# characters in that word.
# The data is stored in a dictionary.

def histogram(word):
    """takes a string and returns a dictionary containing the frequency of
    characters in that word.
    """
    h = {} # initialize an empty dictionary
    for char in word:
        if char in h:
            h[char] +=1
        else:
            h[char] = 1
    return h
    
word = raw_input('Please enter a word: ')

data = histogram(word)

for key, value in data.items():
    print key, value
