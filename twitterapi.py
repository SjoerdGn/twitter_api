# -*- coding: utf-8 -*-
"""
Sjoerd Gnodde

Tell here what it does
"""

# Import everything
import pandas as pd
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
sys.path.insert(0, '../passwords')

import twitter_api_credentials as twit_cred


class TwitterStreamer():
    
    """
    Streaming and processing live tweets
    """
    def __init__(self):
        pass
    
    def stream_tweets(self, save_tweets_filename, substring_check):
        
        # Twitter authentication and the connection 
        # to the Twitter API
        
        listener = StdOutListener(save_tweets_filename)
        auth = OAuthHandler(twit_cred.CONSUMER_KEY, 
                            twit_cred.CONSUMER_SECRET)
        auth.set_access_token(twit_cred.ACCESS_TOKEN, 
                              twit_cred.ACCESS_TOKEN_SECRET)
    
        stream = Stream(auth, listener)
        stream.filter(track=substring_check)

class StdOutListener(StreamListener):
    
    """
    Basic listener. Prints received tweets to standard out.
    """
    
    def __init__(self, save_tweets_filename):
        self.save_tweets_filename = save_tweets_filename
    
    
    def on_data(self, data):
        try:
            print(data)
            with open(self.save_tweets_filename, "a", newline = '') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: {e}".format(e=e))
        return True
    
    def on_error(self, status):
        print(status)
    

if __name__ == "__main__":
    
    # What do I track?
    substring_check = ['pils', 'zuipen', 'beer', 'drinks']
    
    # Where do I save it to
    save_tweets_filename = "output/tweets.json"
    
    # Load streamer
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(save_tweets_filename, substring_check)
    
    
    
"""
password_loc = "../passwords/twitter.csv"

unpw = pd.read_csv(password_loc)


username = unpw['username'][0]
password = unpw['password'][0]
"""