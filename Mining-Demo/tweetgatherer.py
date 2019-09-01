#Import the text pre-process function and a custom stream Listener, as well as API keys. and other needed files
from textpreprocess import preprocess
from streamlistener import MyListener
from Authorize import api
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from Authorize import auth
import json
import termfrequencies
from termfrequencies import stop
import operator
from collections import Counter

# Time limit set to 20 seconds, if undefined defaults to 60
#tweetstream = tweepy.Stream(auth, MyListener(time_limit=20))
#tweetstream.filter(track=['#python'])

from collections import defaultdict
# remember to include the other import from the previous post
 
com = defaultdict(lambda : defaultdict(int))
fname='tweetstream.json'
# Open and analyze the Tweets we pulled.


with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        terms_only = [term for term in preprocess(tweet['text']) 
                    if term not in stop
                    and not term.startswith(('#', '@'))]
    
        # Build co-occurrence matrix
        for i in range(len(terms_only)-1):            
            for j in range(i+1, len(terms_only)):
                w1, w2 = sorted([terms_only[i], terms_only[j]])                
                if w1 != w2:
                    com[w1][w2] += 1

com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])

search_word = 'python' # pass a term as a command-line argument
count_search = Counter()
with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        terms_only = [term for term in preprocess(tweet['text']) 
                    if term not in stop 
                    and not term.startswith(('#', '@'))]
        if search_word in terms_only:
            count_search.update(terms_only)
    print("Co-occurrence for %s:" % search_word)
    print(count_search.most_common(20))