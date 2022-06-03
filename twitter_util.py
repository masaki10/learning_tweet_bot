from requests_oauthlib import OAuth1Session
import config as cf
import tweepy

class TwitterUtil:

    def __init__(self):
        self.client = tweepy.Client(bearer_token    = cf.BEARER_TOKEN,
                           consumer_key    = cf.API_KEY,
                           consumer_secret = cf.API_KEY_SECRET,
                           access_token    = cf.ACCESS_TOKEN,
                           access_token_secret = cf.ACCESS_TOKEN_SECRET,
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
