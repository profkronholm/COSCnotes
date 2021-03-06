# basicfileio.py
# Bill Kronholm
# 2015
# 
# Demonstrates some basic file input and output routines.
# Uses a plain text file called data.csv with the contents below (minus the #s)
#
#Alison Weaver,87426
#Winifred Cannon,83647
#Katie Romero,81853
#Douglas Mendez,42127
#Gilbert Barrett,20495
#Cristina Fitzgerald,63875
#Sherman Powell,99845
#Guillermo Morris,17701
#Moses Hunter,32090
#Colleen Brooks,81041
#

# format for open is as follows:
# open(path/to/file, mode)
# where path/to/file is the path from the current working directory to the file
# given as a string, and the mode can be 'r' for read-only, 'w' for write-only,
# 'a' for appending, and 'r+' for reading and writing.

datafile = open('data.csv', 'r') # open in read-only format
#print 'data file has type', type(datafile)

#data = datafile.read() # read in all of the contents from the file

#print 'data has type', type(data)

#print data

#linesOfData = datafile.readlines()
#print 'linesOfData has type', type(linesOfData)

#print linesOfData

linesOfData = []

for line in datafile:
    linesOfData.append(line)

print linesOfData
datafile.close() # do this with each file you open when you are done with it.

