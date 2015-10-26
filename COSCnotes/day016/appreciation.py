#!/usr/bin/python

from random import randint
import time
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText





adjectives = ['abiding', 'accurate', 'acute', 'adequate',
              'affectionate', 'apparent', 'artistic', 'best',
              'better', 'certain', 'clear',
              'complete', 'comprehensive', 'conscious',
              'considerable', 'constant', 'contemporary', 'cordial', 'correct',
              'critical', 'cultural', 'deep',
              'delicate', 'detailed', 'different', 'discriminating', 'distinct',
              'due', 'eager', 'early', 'earnest', 'emotional',
              'enhanced', 'enlightened', 'enthusiastic', 'equal',
              'evident', 'exact', 'exaggerated', 'express',
              'exquisite', 'fair', 'fine',
              'frank', 'fresh', 'friendly', 'full',
              'future', 'general', 'generous',
              'genial', 'genuine', 'good', 'gradual', 'grateful',
              'great', 'healthy', 'heartfelt',
              'hearty', 'heightened',
              'historical', 'honest', 'human', 'humble', 'humorous',
              'immediate', 'imperfect', 'inadequate', 'instant', 'instinctive',
              'intellectual', 'intelligent', 'intense', 'intimate',
              'intuitive', 'just', 'keen',
              'kindly', 'lasting',
              'literary',
              'lively', 'loving', 'modern',
              'moral', 'musical', 'mutual',
              'natural', 'nice', 'nuanced', 'obvious',
              'particular', 'passionate', 'perfect',
              'personal', 'poetic', 'popular', 'positive',
              'possible', 'practical', 'profound', 'proper', 'public',
              'quick', 'quiet', 'rapid', 'rare', 'rational',
              'ready', 'real', 'realistic', 'refined', 'respectful',
              'reverent', 'right',
              'scholarly', 'scientific', 'sensitive', 'serious', 'shared',
              'similar', 'simple', 'sincere',
              'social', 'sophisticated',
              'sound', 'special', 'spiritual', 'steady', 'strong',
              'subjective', 'substantial', 'subtle', 'such', 'sudden',
              'sufficient', 'sympathetic', 'tender', 'term', 'thorough',
              'true', 'universal', 'unrealized', 'visual',
              'vivid', 'warm',
              'widespread', 'wise', 'wonderful'
              ]

numadj = len(adjectives)
a = randint(0,numadj)
b = randint(0,numadj)

adj1 = adjectives[a]
adj2 = adjectives[b]
n = ''
if adj1[0] in ['a', 'e', 'i', 'o', 'u']: n = 'n'

appreciation = "Thanks for being a%s %s and %s friend." % (n, adj1, adj2)
print appreciation


# Send the message via our own SMTP server, but don't include the
# envelope header.
gmail_user = "my@gmail.com"
gmail_pwd = "like I would give you my real password"
FROM = gmail_user
TO = ['myfriend@internet.biz']
SUBJECT = 'Appreciation for %s' % (time.strftime("%m/%d/%Y"),) # mmddYYYY format
TEXT = appreciation
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" \
          % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
server.sendmail(FROM, TO, message)
#server.quit()
server.close()

s = smtplib.SMTP('localhost')
s.sendmail

