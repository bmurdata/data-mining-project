#Import the text pre-process function and a custom stream Listener, as well as API keys
from textpreprocess import preprocess
from streamlistener import MyListener
from Authorize import api
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from Authorize import auth

tweetstream = tweepy.Stream(auth, MyListener(time_limit=60))
tweetstream.filter(track=['#python'])