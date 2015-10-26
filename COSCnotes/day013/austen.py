# austen.py
# Bill Kronholm
# 2015
#
# Program to show some string and file manipulations.

# chapter 1 of Jane Austen's "Pride and Prejudice" is store in a file called
# pg1342-ch1.txt
# The full text was downloaded from Project Gutenberg: 
# http://www.gutenberg.org/cache/epub/1342/pg1342.txt


with open('pg1342-ch1.txt', 'r') as pridefile:
    """
    Using with ensure the file is closed after the code block below is
    finished.
    """
    chapter1 = pridefile.read()

#chapter1 = chapter1.replace("Lizzy", "Juliet")
#chapter1 = chapter1.replace(" is ", "was") # probably not what you want!
#with open('pg1342-ch1-modified.txt', 'w') as newfile:
#    newfile.write(chapter1)

replacements = {"Lizzy":"Olga", "Bennet":"Inspector Gadget",
                "Bingley":"Ibarra", "Lydia":"12",
                "England":"'merica"}

for name in replacements.keys():
    chapter1 = chapter1.replace(name, replacements[name])

with open('pg1342-ch1-modified.txt', 'w') as newfile:
    newfile.write(chapter1)
