#!/usr/bin/env python3
import praw
from pandas import DataFrame
from dotenv import dotenv_values

# https://towardsdatascience.com/scraping-reddit-data-1c0af3040768

# Load config and create a Reddit instance
config = dotenv_values('.env')
reddit = praw.Reddit(client_id=config['CLIENT_ID'],
                     client_secret=config['CLIENT_SECRET'],
                     user_agent=config['USER_AGENT'])

# Store top 10 posts in a list
top10 = reddit.subreddit('dataengineering').hot(limit=10)
posts = [[post.title, post.score, post.id, post.url,
         post.selftext, post.created] for post in top10]

# Convert posts to DataFrame
columns = ['title', 'score', 'id', 'url', 'body', 'created']
posts = DataFrame(posts, columns=columns)

print(posts)
