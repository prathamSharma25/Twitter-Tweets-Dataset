# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:37:12 2021

@author: Pratham
"""

# Import required libraries
import os
import sys
import pandas as pd
from pandas.io.json import json_normalize
import warnings
warnings.filterwarnings('ignore')

# Get command line arguments for file names
args = list(sys.argv)
directory = args[1]
file_suffix = args[2]
# Set file names
raw_tweets_file = directory + "/farmers-protest-tweets-2021-" + file_suffix + ".json"
tweets_file = directory + "/tweets-2021-" + file_suffix + ".csv"
users_file = directory + "/users-2021-" + file_suffix + ".csv"

# Run snscrape in CLI to get tweets
cmd = "snscrape --progress --jsonl twitter-search \"#FarmersProtest\" > " + raw_tweets_file
os.system(cmd)
    
# read JSON file containing tweets data and remove tweets not in English
raw_tweets = pd.read_json(raw_tweets_file, lines=True)
raw_tweets = raw_tweets[raw_tweets['lang']=='en']

# Normalize 'user' filed, remove less important fields and rename 'id' to 'userId'
users = json_normalize(raw_tweets['user'])
users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)

# Create DataFrame, remove duplicates and save as CSV file
users = pd.DataFrame(users)
users.drop_duplicates(subset=['userId'], inplace=True)
users.to_csv(users_file, index=None)

# Transform 'raw_tweets' DataFrame to get 'tweets' DF
# Add column for 'userId'
user_id = []
for user in raw_tweets['user']:
    uid = user['id']
    user_id.append(uid)
raw_tweets['userId'] = user_id
# Remove less important fields and rename 'id' to 'tweetId'
cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'source', 'media', 'retweetedTweet', 'quotedTweet', 'mentionedUsers']
tweets = raw_tweets[cols]
tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)

# Convert to DataFrame, remove duplicates and save as CSV file
tweets = pd.DataFrame(tweets)
tweets.drop_duplicates(subset=['tweetId'], inplace=True)
tweets.to_csv(tweets_file, index=None)