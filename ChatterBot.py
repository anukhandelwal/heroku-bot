# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "ULInDeesw75ffwbLDuMfrzdmF"
consumer_secret = "uvrBaiG9K9g7n88euhrxZ3yak7LJK2Ax8JefsDbIHXJcLK0hA0"
access_token = "943259924188057600-x1KqIiMjA4lwGC3T4qMcNSwWpdHWTdC"
access_token_secret = "ViRLYv8UGI8vUECTh2sD43gwrm0RO9RAUvVS6Q07eNEJ8"


# Create a function that tweets
# CODE GOES HERE
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1