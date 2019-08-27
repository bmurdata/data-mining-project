import tweepy 
#importing tweepy this is a way to access the twiiter API in python
from tweepy import OAuthHandler
#OAuthHandler is a way to authorize our app

#variables for API keys
consumer_key = "BLUhWnwB3aatDeWFQA0uexECl" 
consumer_secret = "kkHRh2V205lNvw8wE3h19L0L6kefuxWpKc2fK7dN4tg9KqDFKs"
access_token = "1164676256262184963-BHbxcIGihlqkdIQb1mEPt7vJA0gocH"
access_secret = "jBKLOqyaLtV0VWpONjyWNlDJfJmcOoizilCRA27ctFTzf"

#Giving OAuthHandler our private consumer key and consumer secret
auth = OAuthHandler(consumer_key,consumer_secret)
#Accessing token and access secret using auth variable 
auth.set_access_token(access_token,access_secret)

#api variable is the entry point for most of the operations we can perform with Twitter
api = tweepy.API(auth)
# Copied from the Authorize File, in the event that import Authorize fails.

import json
# json is a built in module that allows us to work with JSON data in Python.

for status in tweepy.Cursor(api.home_timeline).items(10):
    
    print(json.dumps(status._json, indent=4)) 
# Above, we run the same code as at the end of Authorize. 
# This time, instead of printing status._json, 
# we use the json.dumps() method to convert it from a Python dictionary
# to a JSON string, with some formatting.

# To avoid being rate limited, the next example will use test-tweet.json, which has a tweet.
# Next, we will import a regular expression library, and define them.
import re
# The regular expression library allows us to find certain patterns called regular
# expressions and do something based off them.
# We will use it to break tweets up, taking into account the structure of tweets.
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 # Emoticon patterns
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
 # regex_str is a full regular expression list of possible patterns.
 # Includes @-mentions, html tags, hash-tags, and emoticons, which are common in tweets.
 # Also has words, and numbers. This gives us a bunch of patterns.
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 # re.compile allows us to store regular expression patterns as objects,
 # which allows us to search a pattern easily.
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 # tokenize finds all the tokens, while preprocess uses it then searches for tokens that
 # are not emoticons and lowercases them.
with open('test-tweet.json', 'r') as f:
        for line in f:
            print(json.dumps(line, indent=4)) 
            tweet = json.loads(line)
            tokens = preprocess(tweet['text'])
            print(tokens)
# Print out the tokens in our test tweet