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
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        subscribers = data['data']['subscribers']
        return (subscribers)
