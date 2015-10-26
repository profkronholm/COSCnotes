# austen3.py
# Bill Kronholm
# 2015
#
# Program to show some string and file manipulations.

# The full text of Jane Austen's "Pride and Prejudice" is store in a file
# called pg1342.txt
# The full text was downloaded from Project Gutenberg: 
# http://www.gutenberg.org/cache/epub/1342/pg1342.txt

import string

with open('pg1342.txt', 'r') as pride:
    fulltext = pride.read()

lowercase = string.lowercase # string of all lowercase letters
uppercase = string.uppercase # string of all uppercase letters

# note, you can get a list of the uppercase and lowercase letters without
# importing the string module
uppercase = map(chr, range(65, 91))
lowercase = map(chr, range(97, 123))

# dictionary to store number of occurances of each letter
frequency = {letter:0 for letter in lowercase+uppercase}

for character in lowercase + uppercase:
    frequency[character] = fulltext.count(character)

for letter in lowercase:
    print letter, frequency[letter] + frequency[letter.upper()]
