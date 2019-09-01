from tweepy import Stream
from tweepy.streaming import StreamListener
import time
#Use the Twitter API to stream in tweets. Will do so by default for 60 seconds, if user doesn't define time limit
class MyListener(StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('tweetstream.json', 'a')
        super(MyListener, self).__init__()

    def on_data(self, data):
        try:
            with open('tweetstream.json', 'a') as f:
                if (time.time() - self.start_time) < self.limit:
                    print('Got a tweet')
                    self.saveFile.write(data)
                    return True
                else:
                    return False

        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True