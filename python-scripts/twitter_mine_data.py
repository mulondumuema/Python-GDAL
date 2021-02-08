import tweepy
import pandas as pd


class tweetApp:
    def __init__(self, consumerkey, consumersecret, accesstoken, accesstokensecret):
        self.consumer_key = consumerkey
        self.consumer_secret = consumersecret
        self.access_token = accesstoken
        self.access_token_secret = accesstokensecret

    def create_api_object(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api

    def get_tweets_yourtimeline(self):
        pub_tweets = self.create_api_object().home_timeline()
        my_tweet = []
        df = pd.DataFrame(my_tweet)
        for tweet in pub_tweets:
            my_tweet.append(tweet)
        return my_tweet, df

    def get_tweets_user(self, userName, numberoftweets):
        id = userName
        count = numberoftweets
        user_tweets = self.create_api_object().user_timeline(id=id, count=count)
        user_tweet = []
        for tweet in user_tweets:
            user_tweet.append(tweet.text)
        return user_tweet

    def get_tweets_keyword(self, keyWords, languageformat='en'):
        q = keyWords
        lang = languageformat
        results = self.create_api_object().search(q=q, lang=lang)
        texttweet = []
        userScreenName = []
        for tweet in results:
            texttweet.append(tweet.text)
            userScreenName.append(tweet.user.screen_name)
        return texttweet, userScreenName


tweet1 = tweetApp(consumerkey="Y3xgpB26eTZkcxp1OMpGwgVg9",
                  consumersecret="SRo9Ex3AgINixd1urrZcsOaJOYwynqhWun2csPz9bRJJctWza6",
                  accesstoken="1084076072973619201-YSYlIK3nm5a4HYuIScNsYxnDJeDIEn",
                  accesstokensecret="YXGy1fn9NZDZ3E1lGyYN27BamQsHaqBubWw4zJkhzFJXJ")
tweetz_user = tweet1.get_tweets_user(userName='MOH_Kenya', numberoftweets=10000)
print(tweetz_user)
#tweets_keyword = tweet1.get_tweets_keyword(keyWords= 'positive')
#print(tweets_keyword)
#tweetz_timeline = tweet1.get_tweets_yourtimeline()
#print(tweetz_timeline)





