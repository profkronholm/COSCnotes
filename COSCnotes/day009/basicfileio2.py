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

def processFile(thefile):
    """Processes a text file with the format of 'name,number\n' and returns
    a list of pairs [name, number]
    Note this function will only work if thefile is a properly formatted text
    document. 
    thefile needs to have been opened ahead of time
    """
    data = []
    for line in thefile:
        line.strip('\n') # remove the \n character from the entry
        entry = line.split(',') # split at the commas. we get [name,number]
        entry[1] = int(entry[1]) # convert number to int type
        data.append(entry)
    return data

def main():
    """ the main program """
    datafile = open('data.csv', 'r') # open in read-only format

    mydata = processFile(datafile)
    print mydata
    for name, number in mydata:
        print name, number
    
    datafile.close()

main()
