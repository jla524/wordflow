#!/usr/bin/env python3
"""
Create a word cloud using text from posts
This may take a while to run
"""
from string import punctuation

import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from wordcloud import WordCloud

from config import Config


def clean_text(text: str) -> str:
    """Remove special characters from text"""
    return ''.join(c for c in text if c not in punctuation)


def make() -> None:
    """Read posts from CSV and generate a word cloud"""
    posts = read_csv(Config.posts_file())
    title = posts['title'].apply(clean_text)
    body = posts['body'].fillna('').apply(clean_text)
    words = np.concatenate((title, body), axis=None)

    wordcloud = WordCloud(width=1600, height=900, background_color='white')
    wordcloud.generate(''.join(words))
    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    Config.image_dir().mkdir(exist_ok=True)
    plt.savefig(Config.wordcloud_file())


if __name__ == '__main__':
    make()
