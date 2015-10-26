#!/usr/bin/python
import os
import time
import tweepy
import random
##################tweepy stuff##########################
CONSUMER_KEY = 'your key here'		
CONSUMER_SECRET = 'your secret here'
ACCESS_KEY = 'your key here'
ACCESS_SECRET = 'your secret here'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def tweetBook():
  bookTitle = 'pg730.txt' # name of file with book in it
  book = open(bookTitle, 'r')
  text = book.read()
  book.close()
  tweet = text[:100] # get first 100 characters
  endChars = [' ', r'.', ',', ':', ';', '!', r'?',')','-',']','\n'] # character indicating end of word
  end = 0
  for endChar in endChars:
    n = tweet.rfind(endChar)
    if n > end: end = n
  if end == 0: end = 100
  tweet = tweet[:end]
  print "tweet has", len(tweet), "characters"
  if len(tweet) > 0:
#    print tweet
    try:
      api.update_status(status = tweet)
      os.remove(bookTitle) # delete old book file
      book = open(bookTitle, 'w')
      book.write(text[end:]) # write remainder of book to file
      book.close()
      tweeted = open(bookTitle+'.twt', 'a') # update book tweeted
      tweeted.write(tweet)
      tweeted.close()
      print tweet
    except Exception as inst:
      print "something went wrong, yo."
      print type(inst)
      print inst
  else:
    print "end of book?"
  text = None	#delete stuff from memory
  tweet = None
  tweeted = None
  book = None
  
if __name__ == "__main__":
  while True:
    tweetBook()
    time.sleep(random.randint(300,3600))
