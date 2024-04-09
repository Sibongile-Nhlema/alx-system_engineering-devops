#!/usr/bin/python3
"""
This module queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces)
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 100,
        "after": after
    } if after else {"limit": 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            # Extract titles from posts and count occurrences of keywords
            for post in posts:
                post_data = post.get('data', {})
                title = post_data.get('title', '').lower()

                # Count occurrences of keywords in the title
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    if keyword_lower in title:
                        counts[keyword_lower] = counts.get(keyword_lower,
                                                           0) + 1

            # Check if there's a next page ('after' token) and recurse
            after = data['data'].get('after')
            if after:
                return count_words(subreddit, word_list,
                                   after=after, counts=counts)

    # Once all pages are processed, print the sorted counts of keywords
    if counts:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for keyword, count in sorted_counts:
            print(f"{keyword}: {count}")
