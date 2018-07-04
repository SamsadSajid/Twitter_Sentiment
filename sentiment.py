from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
# from twitterapistuff import *


#consumer key, consumer secret, access token, access secret.
consumer_key="5EQySd8INekj31s3TEtBL5xpi"
consumer_secret="ihFf09rh9441flBL4sZzd3390WwxbV1DKJDwGD9F7d5lPynRs3"
access_token="2846175301-zfOVIQOG29kZlswVjJYxbLPntJd3lteqzOktIIO"
access_secret="2TEeEddCTqnfaV6zFUvRoxa518LtwCtNOzjQb4HLuKGUh"

class listener(StreamListener):

    def on_data(self, data):
    	all_data = json.loads(data)
    	tweet = all_data["text"]
    	sentiment_value, confidence = s.sentiment(tweet)
    	print(tweet, sentiment_value, confidence)


    	if confidence*100 >= 80:
    		output = open("twitter-out.txt","a")
    		output.write(sentiment_value)
    		output.write('\n')
    		output.close()

    	return True


    def on_error(self, status):
        print(status)

l = listener()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, l)
twitterStream.filter(track=["messi"], languages=["en"])