# moredictionaries.py
# Bill Kronholm
# 2015
# 
# Demonstrates some basic dictionary comprehensions.

#mydict = { x: x**3 for x in [1,4,7]}
#print mydict

fruitList = ['apple', 'banana', 'grape', 'orange', 'kiwi', 'grape']

fruitDict = {name: index for index, name in enumerate(fruitList)}
print fruitDict

#sameFruitDict = dict(enumerate(fruitList)) # convert a list to a dictionary
#print sameFruitDict
