# baderrors.py
# Bill Kronholm
# 2015
#
# Demonstrates some of the errors possible in python.


# Build up to a ZeroDivisionError
#def badidea():
#    return 1/0 # please don't do this!
#    
#try:
#    badidea()
#except Exception as e: 
#    print type(e) # e is a ZeroDivisionError
#    print e.args # tuple containing text description of error
#    print e.message # stuff that typically gets printed to the terminal


# gets an IOError
#try:
#    f = open('noexist.txt', 'r')
#    line = f.readline()
#    f.close()
#    print line
#except Exception as e:
#    print type(e) # e is an IOError
#    print e.args # tuple (x.errno, x.message)
#    print e.message # 
#    # special for IOError
#    print e.errno # number assigned to the specific reason for the error
#    print e.filename # name of file involved
#    print e.strerror # text description for reason for the error
    
#    
# TypeError
#try:
#    a = 5
#    b = 'four'
#    x = a + b
#except Exception as e:
#    print type(e)
#    print e.args
#    print e.message

# NameError    
#try:
#    a = 'a string of some text'
#    print A
#except Exception as e:
#    print type(e)
#    print e.args
#    print e.message
#    
# ValueError
try:
    x = int('this is not an integer at all')
    print x
except Exception as e:
    print type(e)
    print e.args
    print e.message
#    
