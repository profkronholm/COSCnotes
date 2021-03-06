# pointexample.py
# Bill Kronholm
# 2015
#
# Basic usage of the Points.py class, methods, and functions.
#

import Points

P = Points.Point()
Q = Points.Point(2, 3)

print "P has coordinates (%g, %g)" %(P.x, P.y)
print "Q has coordinates (%g, %g)" %(Q.x, Q.y)

R = Points.Point(-4, 2)

d = Points.distance(Q,R)
print "Q and R are distance %g apart" % d

print "R has magnitude %g" % R.magnitude()

S = Points.add(Q,R)
print "Q+R = S = (%g, %g)" % (S.x, S.y)

print Points.subtract(Q, S)
