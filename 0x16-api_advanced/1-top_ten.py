#!/usr/bin/python3
"""T
his module queris the REddit API and prints the first
10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Script that prints the top ten hot
    posts for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    paraams = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=paraams,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return
    else:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print("None")
            return

        for post in posts:
            post_data = post.get("data", {})
            title = post_data.get("title")
            if title:
                print(title)
            else:
                print("Unknown title")
