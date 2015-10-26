# password.py
# Bill Kronholm
# 2015
#
# A program to securely generate a random password using characters
# A-Z, a-z, and 0-9.

import random
import string

def password(n):
    """
    Creates a random string of n alphanumeric characters
    """
    characters = string.ascii_letters + string.digits # alphanumeric chars.
    # SystemRandom is more secure than just random
    #random.seed(15)
    #chars = [random.choice(characters) for i in range(n)]
    chars = [random.SystemRandom().choice(characters) for i in range(n)]
    pw = ''.join(chars)
    return pw

print password(15)

