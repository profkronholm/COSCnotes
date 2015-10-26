import nltk # natural languate toolkit

def fixpunctuation(text):
    newtext = text
    newtext = newtext.replace(' ,', ',')
    newtext = newtext.replace(' .', '.')
    newtext = newtext.replace(' ;', ';')
    newtext = newtext.replace(' :', ':')
    newtext = newtext.replace('( ', '(')
    newtext = newtext.replace(' )', ')')
    newtext = newtext.replace('[ ', '[')
    newtext = newtext.replace(' ]', ']')
    newtext = newtext.replace('{ ', '{')
    newtext = newtext.replace(' }', '}')
    newtext = newtext.replace(' \'', '\'')
    newtext = newtext.replace('` ', '`')
    newtext = newtext.replace(r' ?', r'?')
    newtext = newtext.replace(r' !', r'!')
#    newtext = newtext.replace('Mr. ', 'Mr')
#    newtext = newtext.replace('Ms. ', 'Mrs')
#    newtext = newtext.replace('Ms. ', 'Mrs')
    return newtext

bookdir = '/home/william/dickens/'
bookTitle = 'pg730.txt.noeol' # name of file with book in it
book = open(bookdir + bookTitle, 'r')
oliver = book.read()
book.close()

#oliver = fixpunctuation(oliver)

newtext = ''
for line in oliver.split('\n'):
    tokens = nltk.word_tokenize(line)
    text = nltk.Text(tokens)
    postagged = nltk.pos_tag(tokens)
    ne_chunks = nltk.ne_chunk(postagged)
    words = []
    for chunk in ne_chunks:
        if type(chunk) is nltk.tree.Tree:
            s = '#'
            for c in chunk:
                s += c[0]
            alldots = [i for i, ltr in enumerate(s) if ltr == '.']
            alldots.reverse()
            for i in alldots:
                if i+1 < len(s):
                    if s[i+1] != ' ':
                        s = s[:i] + s[i+1]
            words.append(s)
        else:
            words.append(chunk[0])
    newtext += ' '.join(words)

newtext = fixpunctuation(newtext)
newtext = newtext.replace(r'#Mr. #', '#Mr')

newtext = newtext.replace(r'#Mrs. #', '#Mrs')

newtext = newtext.replace(r'#Ms. #', '#Ms')

newtext = newtext.replace(r'Mrs. ', r'#Mrs')
newtext = newtext.replace(r'Ms. ', r'#Ms')

newtext = newtext.replace(r'#Mrs#', r'#Mrs')
newtext = newtext.replace(r'#Ms#', r'#Ms')



newtext = newtext.replace('##','#')

newbook = open(bookdir + bookTitle + '.ready', 'w')
newbook.write(newtext)
newbook.close()
