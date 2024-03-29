#!/usr/bin/env python3
"""
A reddit scraper to get posts from subreddits
Adapted from https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
"""
from typing import List

from praw import Reddit
from pandas import DataFrame
from dotenv import dotenv_values

from config import Config


def get_reddit() -> Reddit:
    """Load config and create a Reddit instance"""
    config = dotenv_values('/opt/airflow/env/.env')
    instance = Reddit(
        client_id=config['CLIENT_ID'],
        client_secret=config['CLIENT_SECRET'],
        user_agent=config['USER_AGENT']
    )
    return instance


def get_posts(instance: Reddit,
              subreddit: str,
              limit: int = 100) -> List[List]:
    """Store the newest n posts in a list"""
    new_posts = instance.subreddit(subreddit).new(limit=limit)
    results = [[post.title, post.score, post.id, post.url,
                post.selftext, post.created] for post in new_posts]
    return results


def to_frame(results: List[List]) -> DataFrame:
    """Convert results to DataFrame"""
    columns = ['title', 'score', 'id', 'url', 'body', 'created']
    results = DataFrame(results, columns=columns)
    return results


def scrape() -> None:
    """Get post data from r/dataengineering and save as csv"""
    reddit = get_reddit()
    posts = get_posts(reddit, 'dataengineering', limit=25)
    posts = to_frame(posts)

    Config.data_dir().mkdir(exist_ok=True)
    posts.to_csv(Config.posts_file(), index=False)


if __name__ == '__main__':
    scrape()
