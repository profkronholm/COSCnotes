# Points.py
# Bill Kronholm
# 2015
#
# Contains a Point class, methods, and related functions.
#

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
#    # declaring __str__ makes the result of print P to be (P.x, P.y)
#    def __str__(self):
#        return "(%g, %g)" % (self.x, self.y)
#    # define what it means for two instances to be equal and not equal
#    def __eq__(self, other):
#        return (isinstance(other, self.__class__) and
#                self.__dict__ == other.__dict__)
#    def __ne__(self, other):
#        return not self.__eq__(other)

def distance(P,Q):
    """
    expects Point objects P and Q.
    returns the Euclidean distance between the points
    """
    sqdist = (P.x - Q.x)**2 + (P.y - Q.y)**2
    return sqdist**0.5

def add(P, Q):
    """
    does vector addition of points P and Q
    returns a point R with R.x = P.x + Q.x and R.y = P.y + Q.y
    """
    R = Point(P.x + Q.x, P.y + Q.y)
    return R

def negative(P):
    """
    returns point with coordinates negated
    """
    return Point(-P.x, -P.y)

def subtract(P, Q):
    """
    does vector subtraction of points P and Q
    """
    return add(P, negative(Q))

