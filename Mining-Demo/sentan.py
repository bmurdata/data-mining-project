import json
import operator
from collections import Counter
from collections import defaultdict
import math
from termfrequencies import count_all

p_t = {}
com = defaultdict(lambda : defaultdict(int))
p_t_com=defaultdict(lambda : defaultdict(int))

#Count_stop_single is a Counter() sublcass of collections, for counting hashable objects, with .items() a method to return it as a list
#of (elem, cnt) pairs.

#n_docs is number of tweets in the file
with open('tweetstream.json') as f:
    n_docs= sum(1 for _ in f)
print(n_docs)
#Nested for loop, using count_all from termfrequencies. this is a dictionary
#term is the actual term, p_t['Python']=n/17, where n is
for term, n in count_all.items():
    print(term)
    print(n)
    p_t[term] = n / n_docs
    for t2 in com[term]:
        p_t_com[term][t2] = com[term][t2] / n_docs
#p5 and d3
print('Hello p_t')
for x in p_t:
    print("{} has p_t value of: {}".format(x, p_t[x]))
print('Goodbye p_t')

positive_vocab = [
    'good', 'nice', 'great', 'awesome', 'outstanding',
    'fantastic', 'terrific', ':)', ':-)', 'like', 'love','a',
    # shall we also include game-specific terms?
    # 'triumph', 'triumphal', 'triumphant', 'victory', etc.
]
negative_vocab = [
    'bad', 'terrible', 'crap', 'useless', 'hate', ':(', ':-(','no',
    # 'defeat', etc.
]
pmi = defaultdict(lambda : defaultdict(int))
for t1 in p_t:
    for t2 in com[t1]:
        denom = p_t[t1] * p_t[t2]
        pmi[t1][t2] = math.log2(p_t_com[t1][t2] / denom)
 
semantic_orientation = {}

for term, n in p_t.items():
    positive_assoc = sum(pmi[term][tx] for tx in positive_vocab)
    negative_assoc = sum(pmi[term][tx] for tx in negative_vocab)
    semantic_orientation[term] = positive_assoc - negative_assoc

semantic_sorted = sorted(semantic_orientation.items(), 
                         key=operator.itemgetter(1), 
                         reverse=True)
top_pos = semantic_sorted[:10]
top_neg = semantic_sorted[-10:]

print(top_pos)
print(top_neg)
for x in semantic_orientation:
    print("{} semantic orientation: {}".format(x, semantic_orientation[x]))

