import tweepy
import json
import pandas as pd
import s3fs
from datetime import datetime

def run_twitter_etl ():
    # TODO: Replace these with your actual Twitter API credentials
    # Get these from: https://developer.twitter.com/en/portal/dashboard
    access_key = "YOUR_API_KEY_HERE"
    access_secret = "YOUR_API_SECRET_HERE"
    consumer_key = "YOUR_ACCESS_TOKEN_HERE"
    consumer_secret = "YOUR_ACCESS_TOKEN_SECRET_HERE"
    bearer_token = "YOUR_BEARER_TOKEN_HERE"

    # Twitter API v2 Client authentication
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_key,
        access_token_secret=access_secret
    )

    # Get user ID first (required for v2 API)
    user = client.get_user(username='elonmusk')
    user_id = user.data.id

    # Extract tweets from user timeline using v2 API
    tweets = client.get_users_tweets(
        id=user_id,
        max_results=30,  
        exclude='retweets',
        tweet_fields=['created_at', 'text', 'author_id', 'public_metrics']
    )
    # extracting in refined format
    tweet_list = []
    for tweet in tweets.data:
        refined_tweet = {
            'user': user.data.username,
            'text': tweet.text,
            'favorite_count': tweet.public_metrics['like_count'],
            'retweet_count': tweet.public_metrics['retweet_count'],
            'created_at': tweet.created_at
        }
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    # TODO: Replace 'YOUR_BUCKET_NAME' with your actual S3 bucket name
    df.to_csv("s3://YOUR_BUCKET_NAME/elon_musk_twitter_data.csv")



#sample credential as jil are:----jil credential for twitter
#access_key = "ggnfXZnsdAg8YMNFPS1yoS7p0"
 #   access_secret = "sKt961DVcGM6SC1u0d9HGxjXaw44H183AgFsNekeBFFoYlWfe6"
  #  consumer_key = "1944645466706350080-anjMdwiaAtmF0HqKQkqF7R78SYAh2T"
   # consumer_secret = "nLUDNipwuqILgilsFwUbn3OgEbYTuO8tyyjcNa5kJ4iD5"
    #bearer_token = "AAAAAAAAAAAAAAAAAAAAALst5gEAAAAAuWxY9xLEAJTx2R4H9%2FILt0acbsE%3D3uwUolC0GuvzgQGwua0lWeCDiQOIO4TZgBY0sTwhqbOVowCLdk
