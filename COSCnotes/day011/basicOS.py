# basicOS.py
#
# Bill Kronholm
# 2015
#
# Demonstrates some basic use of the os python library.
#

import os # library to interact with the operating system

#cwd = os.getcwd() # the current working directory as a string
#print cwd

#dircontents = os.listdir(cwd) # get file list as a list
#print dircontents

#if 'sample.txt' in dircontents: # check to see if the file exists
#    myfile = open('sample.txt', 'a')
#else:
#    myfile = open('sample.txt', 'w')

#line1 = 'I want this text in my file.\n'
#line2 = 'Followed by this line of text.\n'
#myfile.write(line1)
#myfile.write(line2)
#myfile.close()


# the os.path module handles directory paths
#for item in dircontents:
#    print item, 'is a directory', os.path.isdir(item)


cwd = os.getcwd()
#os.chdir('otherfolder')
os.chdir('..')
print os.listdir(os.getcwd())
#print dircontents

