#using a set of tweets,so the most frequent words should correspond with certain topics.
#We use a custom tokeniser to split the tweets into a list of terms.
from textpreprocess import preprocess
import nltk
from nltk.corpus import stopwords
import string
import operator 
import json
from collections import Counter

nltk.download('stopwords')
#stop-word removal so words aren't actuallly used to convey a particular meaning
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']

fname = 'my-tweets.json'
with open(fname, 'r') as f:
     count_all = Counter()
     for line in f:
         tweet = json.loads(line)
         #Create a list with all the terms
         terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
         #Update the counter
         count_all.update(terms_stop)
         #Print the first 5 most frequent words
         print(count_all.most_common(5))

