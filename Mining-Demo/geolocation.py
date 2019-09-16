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

fname = "tweetstream.json"
# Tweets are stored in "fname"
with open(fname, 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['coordinates']:
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)
 
# Save geo data
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))
