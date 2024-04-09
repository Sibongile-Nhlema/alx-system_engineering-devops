#!/usr/bin/python3
"""
This module returns a list of title of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    script returns the list of titles of all hot
    articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    params = {"limit":100, "after":after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                post_data = post.get('data', {})
                title = post_data.get('title')
                if title:
                    hot_list.append(title)
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after=after)
            else:
                return hot_list
    return None
