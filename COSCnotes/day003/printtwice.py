def printtwice(x):
    print x
    print x
    
#printtwice('hello')
#printtwice('goodbye')

def printstuff(x):
    printtwice(x)
    printtwice(x + ' ' + x)
    
printstuff('stuff')
