#!/usr/bin/python3
"""This module return the total subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
    Script that returns the total number of subscribers
    for a certain subreddit.
    Args:
         -subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;\
               x64) AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    try:
        data = response.json()
        subscribers = data['data']['subscribers']
        return (subscribers)
    except (KeyError, TypeError):
        return 0
