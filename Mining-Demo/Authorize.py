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
#Cursor interface to iterate through different types of objects.
# .items(10) limits the amount of tweets we are reading, however we can access more
# status variable is an instance pf the Status() class
# it's a wrapper to access the data 
# We can also use the same method to see the followers we have
for status in tweepy.Cursor(api.home_timeline).items(10):
#Process a single status 
    print(status._json)

#JSON response from the Twitter API is avaiable in the attribute _json(with a leading under score.)
#Not the raw JSON string, but a dictionary
