# decent hack to remove excess eol characters.

bookTitle = 'pg730.txt' # name of file with book in it
book = open(bookTitle, 'r')
text = book.read()
book.close()

text = text.replace('\r', '') #
text = text.replace('\n', ' ') # all new lines are now spaces.
text = text.replace('  ', '\n') # all double spaces should be new lines
text = text.replace('\n ', '\n') # tweak.
while '\n\n' in text:
    text = text.replace('\n\n', '\n')


newbook = open(bookTitle + '.noeol', 'w')
newbook.write(text)
newbook.close()
