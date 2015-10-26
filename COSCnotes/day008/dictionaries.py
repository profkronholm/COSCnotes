# dictionaries.py
# Bill Kronohlm
# 2015
#
# Demonstrated basic methods and constructors for the dictionary type
#

abbreviation = {
    'California': 'CA',
    'Oregon': 'OR',
    'Washington': 'WA',
    'Nevada': 'NV',
    'Texas': 'RP'
}

#print abbreviation['California']
#print type(abbreviation) # type dict

# add a new entry to the dictionary
abbreviation['Texas'] = 'TX'
#abbreviation[4] = 4
#print abbreviation['TX']

#mykeys = abbreviation.keys() # a list of the available keys
#mykeys.sort()
#print mykeys

## print them all out
#for key in abbreviation.keys():
#    print "The abbreviation for %s is %s" % (key, abbreviation[key])

## same output as previous
#for state, abbr in abbreviation.items():
#    print "The abbreviation for %s is %s" % (state, abbr)
    
## remove keys and their values with del

#del abbreviation['Nevada']

#for key, value in abbreviation.items():
#    print "The abbreviation for %s is %s" % (key, value)

## check if a particular key exists
print 'CA' in abbreviation

