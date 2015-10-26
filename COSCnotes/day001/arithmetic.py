# arithmetic.py
# demonstrates some basic arithmetic for different number types.
#
#

x = 42 # this is an integer type
y = 9 # also an integer

print "the sum of x and y is x + y =", x + y

print "the product of x and y is x * y =", x * y

print "the difference of x and y is x - y =", x - y

print "x raised to the power y is x**y =", x**y


# the result of integer arithmetic is always an integer
print "the quotient of x and y is x/y =", x/y

# we use % for remainders
print "the remainder when x is divided by y is", x%y


print "x has type" type(x) # x is an integer

z = 9.0 # this is a float (or floating-point number)
print "z has type", type(z)

# the product/quotient of an integer and a float is a float
print "the product of x and z is x*z", x*z, "which has type", type(x*z)
print "the quotient of x and z is x/z", x/z


