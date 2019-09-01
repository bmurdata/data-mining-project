import json
# remember to include the other import from the previous post
 

fname='tweetstream.json'
# Open and analyze the Tweets we pulled.
#possible_json_string = str(data) #original error
possible_json_string = '{}' #sanity check with simplest json
#possible_json_string = data #why convert to string at all?
#possible_json_string = data.decode('utf-8') #intentional conversion
data = []



with open(fname,'r') as f:

    for line in f:
        poke=str(line)
        print(poke)
        print(line)
        tweep = json.loads(poke)
        print(tweep)