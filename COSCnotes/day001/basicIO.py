# basicIO.py
# demonstrates some basic user input
#
#

# get values from the user
x = raw_input('Enter an integer: ')
print "You entered", x, "which has type", type(x) # type(x) is str

y = int(x) # change x to an integer, if possible

print "I changed it to an integer", y, type(y)

z = raw_input('Enter another integer: ')
w = int(z)

print "the sum of your numbers is", y+w

print x+z
