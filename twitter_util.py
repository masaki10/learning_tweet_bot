from requests_oauthlib import OAuth1Session
import tweepy
import os

class TwitterUtil:

    def __init__(self):
        self.client = tweepy.Client(bearer_token    = os.environ["BEARER_TOKEN"],
                           consumer_key    = os.environ["API_KEY"],
                           consumer_secret = os.environ["API_KEY_SECRET"],
                           access_token    = os.environ["ACCESS_TOKEN"],
                           access_token_secret = os.environ["ACCESS_TOKEN_SECRET"],
                          )

    def post(self, content):
        res = self.client.create_tweet(text=content)
        print(res)

    def get_tweets_from_user(self, user_id):
        res = self.client.get_users_tweets(id=user_id, max_results=100, exclude="retweets")
        # print(res.data)
        # print(len(res.data))
        # print(res.data[0])
        # print(res.data[0].id)
        # raise
        return res.data
