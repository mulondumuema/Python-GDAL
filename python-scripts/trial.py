import tweepy

auth = tweepy.OAuthHandler("Y3xgpB26eTZkcxp1OMpGwgVg9", "SRo9Ex3AgINixd1urrZcsOaJOYwynqhWun2csPz9bRJJctWza6")
auth.set_access_token("1084076072973619201-YSYlIK3nm5a4HYuIScNsYxnDJeDIEn", "YXGy1fn9NZDZ3E1lGyYN27BamQsHaqBubWw4zJkhzFJXJ")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)