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


def clean_text(text: str) -> str:
    """Remove special characters from text"""
    return ''.join(c for c in text if c not in punctuation)


if __name__ == '__main__':
    posts = read_csv('posts.csv')

    # Store title and body text into numpy array
    title = posts['title'].apply(clean_text)
    body = posts['body'].fillna('').apply(clean_text)
    words = np.concatenate((title, body), axis=None)

    # Create and display word cloud
    wc = WordCloud(width=1600, height=900, background_color='white')
    wc.generate(''.join(words))
    plt.figure(figsize=(16, 9))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()
