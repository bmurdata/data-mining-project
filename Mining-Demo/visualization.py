#birdges the gap between a python back-end and a front-end that supports D3.js visualisation

import vincent

from termfrequencies import count_all
word_freq = count_all.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx = 'x')
bar.to_json('tweetstream.json')
