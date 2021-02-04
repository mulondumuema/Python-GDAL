import tweepy
import pandas as pd

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '3175535685-47C5IYW3awv8Q6o5rqyPqGxRagBbWinNd7RBjFL'
ACCESS_SECRET = 'jfDJRhwSh9M7fLY67KiKQSv8lhLakxVxFf9dSazJvZtLD'
CONSUMER_KEY = 'hgK2LtQ33wgICcHU2NGWOboZz'
CONSUMER_SECRET = 'UM3kSsSu0QFVi43HSkiDh2SL3Q4uFY22Uf63zZkmb3IOgAIfRL'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuth()

# tweets from my stream
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

# tweets from a specific user
trump_tweets = api.user_timeline('MOH_Kenya')
#for tweet in trump_tweets:
#    print(tweet.text)


# fuction to extract data from tweet object
def extract_tweet_attributes(tweet_object):
    # create empty list
    tweet_list =[]
    # loop through tweet objects
    for tweet in tweet_object:
        tweet_id = tweet.id # unique integer identifier for tweet
        text = tweet.text # utf-8 text of tweet
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at # utc time tweet created
        source = tweet.source # utility used to post tweet
        reply_to_status = tweet.in_reply_to_status_id # if reply int of orginal tweet id
        reply_to_user = tweet.in_reply_to_screen_name # if reply original tweetes screenname
        retweets = tweet.retweet_count # number of times this tweet retweeted
        favorites = tweet.favorite_count # number of time this tweet liked
        # append attributes to list
        tweet_list.append({'tweet_id':tweet_id,
                          'text':text,
                          'favorite_count':favorite_count,
                          'retweet_count':retweet_count,
                          'created_at':created_at,
                          'source':source,
                          'reply_to_status':reply_to_status,
                          'reply_to_user':reply_to_user,
                          'retweets':retweets,
                          'favorites':favorites})
    # create dataframe
    df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                           'text',
                                           'favorite_count',
                                           'retweet_count',
                                           'created_at',
                                           'source',
                                           'reply_to_status',
                                           'reply_to_user',
                                           'retweets',
                                           'favorites'])
    return df

df = extract_tweet_attributes(trump_tweets)
print(df)


